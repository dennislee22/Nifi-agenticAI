# Nifi in Agentic AI

![nifi-agenticAI](https://github.com/user-attachments/assets/1bceb23c-9362-4199-844d-c05458837aa5)



```
curl -X 'POST'  'https://malay-deberta.cml.apps.company.com/predict/' -H 'Content-Type: application/json' -d '{"text": "kamu sangat comel"}'
{"sentiment":[{"label":"positive","score":0.994461178779602}]}

curl -X 'POST'  'https://malay-deberta.cml.apps.company.com/predict/' -H 'Content-Type: application/json' -d '{"text": "saya tak comel"}'
{"sentiment":[{"label":"negative","score":0.9951584935188293}]}
```

<img width="1019" alt="image" src="https://github.com/user-attachments/assets/9598d99d-bcbc-4ac6-a4c4-c74e53b916d0" />

<img width="723" alt="image" src="https://github.com/user-attachments/assets/c3bb9937-86fa-49d3-a9d6-e8fb6fe267e2" />

<img width="720" alt="image" src="https://github.com/user-attachments/assets/aa280c6d-aec0-4db1-b0b0-82fa79d29c8b" />

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/24327c89-5a67-4651-b3bc-f4073d8a89fa" />

<img width="720" alt="image" src="https://github.com/user-attachments/assets/b62ea6ab-201a-4e90-b22e-847380b3fa2d" />



```
INSERT INTO sentiment_data (sentiment_label, sentiment_score) VALUES ('${sentiment_label}', ${sentiment_score});
```

<img width="1118" alt="image" src="https://github.com/user-attachments/assets/e0bdbe62-1048-4de8-8c2e-7b290e0c85c0" />





<img width="1429" alt="image" src="https://github.com/user-attachments/assets/14399099-1bca-4186-af6e-c057f7cb913e" />

```
SELECT 
  time AS "time",  
  CASE 
    WHEN sentiment_label = 'negative' THEN 1
    WHEN sentiment_label = 'positive' THEN 2
    ELSE 0
  END AS "White=Negative
  Maroon=Positive"
FROM sentiment_data
WHERE time >= now() - interval '5 minutes'
ORDER BY time;
```
