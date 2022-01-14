import boto3
import pprint
from os import path

# Translate service client
translate = boto3.client('translate')
basepath = path.dirname(__file__)

with open(path.join(basepath, 'terms.csv')) as file:
    translate.import_terminology(
        Name='term_en',
        MergeStrategy='OVERWRITE',
        TerminologyData={'File': file.read(), 'Format': 'CSV'}
    )


def run(text):
    pprint.pprint(translate.list_terminologies())

    result = translate.translate_text(
        Text=text,
        SourceLanguageCode='en',
        TargetLanguageCode='ja',
        TerminologyNames=['term_en'])
    pprint.pprint(result)
    print(result['TranslatedText'])


if __name__ == '__main__':
    text = 'Godspeed You! Black Emperor (sometimes abbreviated to GY!BE) is a Canadian post-rock band which originated in Montreal, Quebec in 1994. The group releases recordings through Constellation, an independent record label also located in Montreal.'
    run(text)
