# Nifi in Agentic AI

![nifi-agenticAI](https://github.com/user-attachments/assets/1bceb23c-9362-4199-844d-c05458837aa5)

In an **Agentic AI** system, `Perception` tools transform raw input into structured signals for `Reasoning` engine. Apache NiFi fits this role seamlessly, thanks to its visual, flow-based architecture and powerful integration capabilities. Here's the Agentic AI demo that illustrates how NiFi can effortlessly construct a real-time data pipeline for live marketing scenarios on social media platform. The business use case involves analyzing audience feedback from incoming comments in real time, allowing the promoter to swiftly adjust their strategy based on the results of the sentiment analysis, e.g. positive or negative.

## <a name="toc_1"></a>Perception
During a livestream product promotion, user comments are ingested in real time and sent to a Kafka topic. NiFi’s `ConsumeKafka` processor subscribes to this stream and pulls the comments into Nifi FlowFiles. 

<img width="1019" alt="image" src="https://github.com/user-attachments/assets/9598d99d-bcbc-4ac6-a4c4-c74e53b916d0" />

These are passed to an `InvokeHTTP` processor, which sends them to an Cloudera AI (CAI) platform acting as the [Reasoning](#toc_2) engine. NiFi’s `EvaluateJsonPath` processor extracts the sentiment label and score from the JSON and promotes them to attributes. 

<img width="723" alt="image" src="https://github.com/user-attachments/assets/c3bb9937-86fa-49d3-a9d6-e8fb6fe267e2" /><br>

The `PutSQL` processor then sinks these records into a PostgreSQL database, using JDBC connection with the following SQL command.
```
INSERT INTO sentiment_data (sentiment_label, sentiment_score) VALUES ('${sentiment_label}', ${sentiment_score});
```

<img width="720" alt="image" src="https://github.com/user-attachments/assets/aa280c6d-aec0-4db1-b0b0-82fa79d29c8b" /><br>

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/24327c89-5a67-4651-b3bc-f4073d8a89fa" /><br>

<img width="720" alt="image" src="https://github.com/user-attachments/assets/b62ea6ab-201a-4e90-b22e-847380b3fa2d" /><br>

Here's the sample of the table records that have been inserted by the Nifi's `PutSQL` processor.
<img width="1118" alt="image" src="https://github.com/user-attachments/assets/e0bdbe62-1048-4de8-8c2e-7b290e0c85c0" /><br>

## <a name="toc_2"></a>Reasoning
The platform uses **FastAPI** to expose an inference API powered by a Transformer-based AI model. Clients send user comments (in a specific language), and the model returns analysis results, such as sentiment or classification.

<img width="658" alt="image" src="https://github.com/user-attachments/assets/35c4aad2-2ec4-493a-be05-256ab364d0ed" /><br>

The model analyzes the sentiment and returns a structured JSON payload, for example:

```
curl -X 'POST'  'https://malay-deberta.cml.apps.company.com/predict/' -H 'Content-Type: application/json' -d '{"text": "kamu sangat comel"}'
{"sentiment":[{"label":"positive","score":0.994461178779602}]}

curl -X 'POST'  'https://malay-deberta.cml.apps.company.com/predict/' -H 'Content-Type: application/json' -d '{"text": "saya tak comel"}'
{"sentiment":[{"label":"negative","score":0.9951584935188293}]}
```

## Feedback Presentation
Grafana connects to PostgreSQL and visualizes the sentiment labels in real time, offering live feedback on how viewers are reacting to the promotion.

<img width="1429" alt="image" src="https://github.com/user-attachments/assets/14399099-1bca-4186-af6e-c057f7cb913e" /><br>

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

This end-to-end demo showcases how NiFi enables rapid development of real-time, agentic AI pipelines—bridging perception, reasoning, and action in dynamic marketing environments.

