![](https://raw.githubusercontent.com/gabrielfernando01/x-sentiment-spark-free/main/images/cover_readme.png)

# X Sentiment Analysis with Spark (AWS Free Tier).

This project analyzes sentiment in X (Twitter) posts about a political figure (e.g., "Donald Trump") or event (e.g., "2024 elections") using Apache Spark 💥 in Scala 🟥. It counts sentiments (positive, negative, neutral) per day and stores results in AWS S3, all within the AWS Free Tier for educational purposes.

- **Objective**: Learn Spark 💥, Scala 🟥, and AWS data workflows ☁️.
- **Dataset**: Public X posts (1-2 GB, within S3's 5 GB free tier).
- **Processing**: Spark 3.5.1 on an EC2 t2.micro instance (no EMR).
- **Storage**: S3 buckets for input and output.
- **Repo**: `x-sentiment-spark-free`.

## Prerequisites

- 💻 **Hardware**: 16 GB RAM, 200 GB storage.
- 🐧 **OS**: Kubuntu 24.04.1, Kernel 6.8.0-52-generic.
- ☕ **Java**: OpenJDK 11 (`/usr/lib/jvm/java-11-openjdk-amd64`).
- 🟥 **Scala**: 2.13.8 (`/usr/local/share/scala`).
- 💥 **Spark**: 3.5.1 (`/opt/spark`).
- 🔌 **Tools**: SBT 1.10.7, Maven 3.8.7, IntelliJ IDEA 24.04.
- ☁️ **AWS**: Free Tier account (40 days remaining as of 13/03/2025).
- 😼 **GitHub**: Existing account.
