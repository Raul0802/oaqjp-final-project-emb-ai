import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # 1. Converte o texto da resposta em um dicionário
    formatted_response = json.loads(response.text)
    
    # 3. Extrai o conjunto de emoções exigido
    # (A estrutura padrão do Watson guarda as emoções neste caminho)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 4. Lógica para encontrar a emoção dominante
    # Cria um dicionário apenas com as emoções para facilitar a busca do valor máximo
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Retorna a chave (nome da emoção) que tem o maior valor (score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # 5. Retorna no formato exato solicitado
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }