import boto3
from os import path

translate = boto3.client('translate')
basepath = path.dirname(__file__)

with open(path.join(basepath, 'trans.txt')) as file_in:
    with open(path.join(basepath, 'trans_out.txt'), 'w') as file_out:
        for text in file_in:
            if text != '\n':
                result = translate.translate_text(
                    Text=text, SourceLanguageCode='en', TargetLanguageCode='ja')
                file_out.write(result['TranslatedText'])
            file_out.write('\n')
