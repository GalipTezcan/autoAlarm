import os
import html
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="upload_video.py-oauth2.json"
# Instantiates a client
client = texttospeech.TextToSpeechClient()
with open("erkek.txt","r",encoding="utf-8") as f:
    isimler=["Sümeyye"]
    for i in isimler:


        def text_to_ssml(inputfile):
            raw_lines = inputfile

            # Replace special characters with HTML Ampersand Character Codes
            # These Codes prevent the API from confusing text with
            # SSML commands
            # For example, '<' --> '&lt;' and '&' --> '&amp;'

            escaped_lines = html.escape(raw_lines)

            # Convert plaintext to SSML
            # Wait two seconds between each address
            ssml = "<speak>{}</speak>".format(
                escaped_lines.replace("\n", '\n<break time="1s"/>'),
                escaped_lines.replace(".",'<break time="0.1s"/>'),
                escaped_lines.replace(",", '<break time="0.05s"/>')
            )

            # Return the concatenated string of ssml script
            return ssml


        text = f"""
        Sümeyye
        Sümeyye
        Sümeyye
        Sümeyye kalk hadi
        Sümeyye
        Şimdi kalkmazsan seni kimse kaldırmayacak Sümeyye
        Yapacağın şeyleri kaçırıyorsun
        Tekrar uyursan her şey için çok geç olacak Sümeyye
        o yüzden kalk artık Sümeyye
        Sümeyye
        Hadi Sümeyye uyan artık
"""

        ssml = text_to_ssml(text)
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code="tr-TR", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="tr-TR-Wavenet-A"
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            speaking_rate=0.9,
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # The response's audio_content is binary.
        with open(f"Sümeyye_kiz.mp3", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print(f'Audio content written to file Sümeyye_kiz')
