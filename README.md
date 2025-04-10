# Nifi in Agentic AI


![e2e-malaytwits-nifi-cai](https://github.com/user-attachments/assets/43eea365-494e-46a5-b330-70fd20d2e327)


```
curl -X 'POST'  'https://malay-deberta.goes-ocp-cml.apps.field-team-ocp-01.kcloud.cloudera.com/predict/' -H 'Content-Type: application/json' -d '{"text": "saya sangat comel"}'
{"sentiment":[{"label":"positive","score":0.994461178779602}]}

curl -X 'POST'  'https://malay-deberta.goes-ocp-cml.apps.field-team-ocp-01.kcloud.cloudera.com/predict/' -H 'Content-Type: application/json' -d '{"text": "saya tak comel"}'
{"sentiment":[{"label":"negative","score":0.9951584935188293}]}
```
