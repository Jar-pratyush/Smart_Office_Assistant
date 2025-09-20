from groq import Groq
def get_email_text():
    """
    This function will take the email text from the user as input and return the text as string 
    """

    email_text = input("Enter the email text:\n")

    return email_text

def get_bullet_points():
    """
    This funciton will take the bullet points that must be there in the email in a comma separted format and return the list of points without any whitespaces and removing all points which become empty after stripping the whitespaces.
    """

    bullet_points = input("Enter the bullet points as comma separated values:\n")
    points = [point.strip() for point in bullet_points.split(",") if point.strip()]
    return points

def choose_tone():
    "Asks the user to choose one of the four tones for input in prompt. The tones are mapped in the form of dictionary."

    tone_options = {1:"formal",2:"friendly",3:"concise",4:"deatiled"}
    print(f"Choose a tone option:\n1. {tone_options.get(1)}\n2. {tone_options.get(2)}\n3. {tone_options.get(3)}\n4. {tone_options.get(4)}")
    try:
        user_tone_choice = int(input("Enter a choice 1-4:\n"))
        return tone_options.get(user_tone_choice,"formal")
    except ValueError:
        return "formal"
    
def build_prompt(email_text, bullet_points, tone):
    """
    Constructing the final prompt using all the inputs
    """
    bullet_point_str = ", ".join(bullet_points)
    return f"Draft a professional email reply in a {tone} tone based on the following.\n Original email: {email_text}\n Key Points to include: {bullet_point_str}\n Reply:" 

def generate_reply(prompt,api_key):
    """
    The prompt is collected and then sent to groq and the reply is stripped and returned.
    """
    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [{"role":"user","content":prompt}],
        temperature = 0.3,
        max_completion_tokens = 512
    )
    return chat_completion.choices[0].message.content.strip()

def get_api_key():
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY") 
    return api_key

if __name__ == "__main__":
    # Get the original text from the user from email
    email_text = get_email_text()
    # Get bullet points from the user
    bullet_points = get_bullet_points()
    # Get the desired reply tone
    tone = choose_tone()
    # Final Prompt
    prompt = build_prompt(email_text, bullet_points, tone)
    # Display the generated prompt
    print("\nGenerated Prompt:\n",prompt)
    # Retrive the API-KEY from .env
    api_key = get_api_key()

    #Call the Groq for reply
    try:
        reply = generate_reply(prompt,api_key)
        print("\nDrafted Reply:\n",reply)
    except Exception as e:
        print(f"Error: {e}")