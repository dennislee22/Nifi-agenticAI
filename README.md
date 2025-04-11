# Nifi in Agentic AI

![nifi-agenticAI](https://github.com/user-attachments/assets/1bceb23c-9362-4199-844d-c05458837aa5)



```
curl -X 'POST'  'https://malay-deberta.goes-ocp-cml.apps.field-team-ocp-01.kcloud.cloudera.com/predict/' -H 'Content-Type: application/json' -d '{"text": "saya sangat comel"}'
{"sentiment":[{"label":"positive","score":0.994461178779602}]}

curl -X 'POST'  'https://malay-deberta.goes-ocp-cml.apps.field-team-ocp-01.kcloud.cloudera.com/predict/' -H 'Content-Type: application/json' -d '{"text": "saya tak comel"}'
{"sentiment":[{"label":"negative","score":0.9951584935188293}]}
```

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
