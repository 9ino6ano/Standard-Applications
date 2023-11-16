from googletrans import Translator
from textblob import TextBlob
import

# Using googletrans
translator = Translator()
result = translator.translate("Hello", dest='es')
print(result.text)

# Using textblob
text = "This is a simple example."
blob = TextBlob(text)
print(blob.translate(to='es'))
