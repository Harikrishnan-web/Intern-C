import os
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

import requests
from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

# ----------------------------------------------------------------------
# SETTINGS (change model names here if a provider retires one)
# ----------------------------------------------------------------------
GEMINI_MODEL = "gemini-2.5-flash"
GROQ_MODEL = "openai/gpt-oss-20b"
VIDEO_MODEL = "Wan-AI/Wan2.2-T2V-A14B"             # experimental, may be unavailable

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

LINE = "=" * 55


# ----------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------
def header(title):
    print("\n" + LINE)
    print(title)
    print(LINE)


def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def choose_provider():
    header("SELECT AI PROVIDER (for text / prompt enhancement)")
    print("1. Google Gemini")
    print("2. Groq")
    while True:
        choice = input("\nChoose provider (1/2): ").strip()
        if choice in ("1", "2"):
            return choice
        print("Please enter 1 or 2.")


# ----------------------------------------------------------------------
# TEXT MODELS (Gemini / Groq) WITH RETRIES
# ----------------------------------------------------------------------
def generate_response(choice, prompt):
    for attempt in range(3):
        try:
            if choice == "1":
                api_key = os.getenv("GEMINI_API_KEY")
                if not api_key:
                    raise ValueError("Gemini API key missing in .env")

                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model=GEMINI_MODEL, contents=prompt
                )
                return response.text or "No response received."

            elif choice == "2":
                api_key = os.getenv("GROQ_API_KEY")
                if not api_key:
                    raise ValueError("Groq API key missing in .env")

                client = Groq(api_key=api_key)
                response = client.chat.completions.create(
                    model=GROQ_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_completion_tokens=2000,
                )
                return response.choices[0].message.content or "No response received."

            else:
                raise ValueError("Invalid provider selection.")

        except Exception as error:
            if attempt == 2:
                raise
            print(f"\nTemporary error: {error}\nRetrying ({attempt + 1}/2)...")
            time.sleep(2 ** attempt)


# ----------------------------------------------------------------------
# MODE 1: TEXT (your original six-question flow)
# ----------------------------------------------------------------------
def build_text_prompt():
    questions = {
        "TASK": "What should the AI do?",
        "ROLE": "What role should the AI take?",
        "CONTEXT": "What background information is needed?",
        "CONSTRAINTS": "What rules should the AI follow?",
        "OUTPUT": "What format should the answer have?",
        "EXAMPLE": "Give an example of the expected result.",
    }

    answers = {}
    print("\nAnswer the following six questions:\n")

    for section, question in questions.items():
        value = input(f"{section} - {question}\n> ").strip()
        if not value:
            print(f"\nError: {section} cannot be empty.")
            return None
        answers[section] = value

    return f"""
You are an expert prompt-following AI assistant.

Complete the task using these specifications.

TASK:
{answers['TASK']}

ROLE:
{answers['ROLE']}

CONTEXT:
{answers['CONTEXT']}

CONSTRAINTS:
{answers['CONSTRAINTS']}

EXPECTED OUTPUT:
{answers['OUTPUT']}

EXAMPLE:
{answers['EXAMPLE']}

INSTRUCTIONS:
- Understand all six sections before answering.
- Follow the specified role and context.
- Follow all constraints strictly.
- Use the requested output format.
- Treat the example as a guide.
- Identify missing information when necessary.
- Never invent facts or unsupported information.
- Provide a clear, accurate and relevant response.
"""


def run_text_mode():
    prompt = build_text_prompt()
    if prompt is None:
        return

    result_file = OUTPUT_DIR / f"text_{timestamp()}.txt"
    result_file.write_text("GENERATED PROMPT\n" + LINE + "\n" + prompt, encoding="utf-8")

    header("GENERATED PROMPT")
    print(prompt)

    provider = choose_provider()

    try:
        print("\nConnecting to AI provider...")
        answer = generate_response(provider, prompt)

        header("AI RESPONSE")
        print(answer)

        with open(result_file, "a", encoding="utf-8") as f:
            f.write("\n\nAI RESPONSE\n" + LINE + "\n" + answer)

        print(f"\nSuccessfully completed! Saved to {result_file}")

    except Exception as error:
        print("\nAI PROVIDER ERROR")
        print(f"{type(error).__name__}: {error}")
        print(f"\nYour generated prompt is saved in {result_file}")


# ----------------------------------------------------------------------
# PROMPT ENHANCER FOR IMAGE / VIDEO
# ----------------------------------------------------------------------
def enhance_visual_prompt(kind, description, provider):
    """Uses Gemini/Groq (free) to turn a short idea into a detailed prompt."""
    if kind == "image":
        extra = "subject, style, lighting, colours, composition, camera angle and mood"
    else:
        extra = "subject, action, camera movement, lighting, style, setting and mood"

    request = f"""
You are an expert prompt engineer for AI {kind} generation models.

Rewrite the user's idea into ONE detailed {kind} generation prompt.
Include: {extra}.
Do not invent unrelated elements. Keep it under 120 words.
Return ONLY the final prompt text, with no explanation or quotes.

USER IDEA:
{description}
"""
    return generate_response(provider, request).strip()


# ----------------------------------------------------------------------
# MODE 2: IMAGE (free: Hugging Face Inference, FLUX.1-schnell)
# ----------------------------------------------------------------------
def generate_image(prompt):
    """Free, no API key needed. Anonymous use is rate-limited (about 1 request
    per 15 seconds) and images may carry a small watermark."""
    url = "https://image.pollinations.ai/prompt/" + quote(prompt)
    params = {"width": 1024, "height": 1024, "nologo": "true"}

    for attempt in range(3):
        response = requests.get(url, params=params, timeout=120)

        if response.status_code == 200 and response.content:
            path = OUTPUT_DIR / f"image_{timestamp()}.jpg"
            path.write_bytes(response.content)
            return path

        if response.status_code == 429 and attempt < 2:
            print("Free service is busy (rate limit). Waiting 20 seconds...")
            time.sleep(20)
            continue

        raise RuntimeError(
            f"Image service returned status {response.status_code}. "
            "Wait a minute and try again."
        )


# ----------------------------------------------------------------------
# MODE 3: VIDEO (experimental: free access is limited)
# ----------------------------------------------------------------------
def generate_video(prompt):
    token = os.getenv("HF_TOKEN")
    if not token:
        raise ValueError("HF_TOKEN missing in .env (free token from huggingface.co)")

    from huggingface_hub import InferenceClient

    client = InferenceClient(api_key=token)
    video_bytes = client.text_to_video(prompt, model=VIDEO_MODEL)

    path = OUTPUT_DIR / f"video_{timestamp()}.mp4"
    path.write_bytes(video_bytes)
    return path


def run_visual_mode(kind):
    description = input(f"\nDescribe the {kind} you want:\n> ").strip()
    if not description:
        print("\nError: description cannot be empty.")
        return

    provider = choose_provider()

    try:
        print("\nEnhancing your description into a detailed prompt...")
        enhanced = enhance_visual_prompt(kind, description, provider)

        header(f"ENHANCED {kind.upper()} PROMPT")
        print(enhanced)

        prompt_file = OUTPUT_DIR / f"{kind}_prompt_{timestamp()}.txt"
        prompt_file.write_text(enhanced, encoding="utf-8")

        print(f"\nGenerating {kind}... (this can take a while)")
        path = generate_image(enhanced) if kind == "image" else generate_video(enhanced)

        print(f"\nSuccessfully completed! {kind.capitalize()} saved to {path}")

    except Exception as error:
        print(f"\n{kind.upper()} GENERATION ERROR")
        print(f"{type(error).__name__}: {error}")
        if kind == "video":
            print("\nFree video generation is not reliably available. If the error "
                  "mentions payment or credits (402), the free allowance is used up. "
                  "Your enhanced prompt is still saved in the outputs folder, so you "
                  "can paste it into a free web video tool.")


# ----------------------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------------------
def main():
    print(LINE)
    print("       AI PROMPT ENGINEERING ASSISTANT")
    print(LINE)

    while True:
        header("WHAT WOULD YOU LIKE TO GENERATE?")
        print("1. Paragraph text")
        print("2. Image")
        print("3. Video (experimental)")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            run_text_mode()
        elif choice == "2":
            run_visual_mode("image")
        elif choice == "3":
            run_visual_mode("video")
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()