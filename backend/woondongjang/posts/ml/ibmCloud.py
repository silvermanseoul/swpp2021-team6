import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions


def keyword_extraction_ML(text):
    authenticator = IAMAuthenticator("RUfaiN4C2iFxOwHspcFekE022wkEzoW7EnSgSb2KtRgO")
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version="2021-08-01", authenticator=authenticator
    )

    natural_language_understanding.set_service_url(
        "https://api.kr-seo.natural-language-understanding.watson.cloud.ibm.com/instances/572ce3ab-5aa8-4de7-bec4-db85f624d062"
    )

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
            keywords=KeywordsOptions(sentiment=True, emotion=True, limit=3)
        ),
    ).get_result()

    results = json.dumps(response, indent=2, ensure_ascii=False)
    json_data = json.loads(results)
    return [each["text"] for each in json_data["keywords"]]


# test_text = """안녕하세요~ 이번 주말에 잠실에서 축구 함께 하실 분 구하고 있습니다!
#         저희가 다 활발한 편이어서 MBTI E에 해당하는 분들이 오시면 좋을 것 같아요!
#         뒷풀이도 예정하고 있으니 많은 참여 부탁드립니다!"""
# keyword_extraction_ML(test_text)
