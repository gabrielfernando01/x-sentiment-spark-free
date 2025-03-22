![](https://raw.githubusercontent.com/gabrielfernando01/x-sentiment-spark-free/main/image/cover_readme.png)

# X Sentiment Analysis with Spark 💥 (AWS ☁️ Free Tier).

This project analyzes sentiment in X (Twitter) posts about a political figure (e.g., "Donald Trump") or event (e.g., "2024 elections") using Apache Spark 💥 in Scala 🟥. It counts sentiments (positive, negative, neutral) per day and stores results in AWS S3, all within the AWS Free Tier for educational purposes.

- **Objective**: Learn Spark 💥, Scala 🟥, and AWS data workflows ☁️.
- **Dataset**: Public X posts (1-2 GB, within S3's 5 GB free tier).
- **Processing**: Spark 3.5.1 on an EC2 <code>t2.micro</code> instance (no EMR).
- **Storage**: S3 buckets 🪣 for input and output.
- **Repo**: `x-sentiment-spark-free`.

## Prerequisites.

- 💻 **Hardware**: 16 GB RAM, 200 GB storage.
- 🐧 **OS**: Kubuntu 24.04.1, Kernel 6.8.0-52-generic.
- ☕ **Java**: OpenJDK 11 (`/usr/lib/jvm/java-11-openjdk-amd64`).
- 🟥 **Scala**: 2.13.8 (`/usr/local/share/scala`).
- 💥 **Spark**: 3.5.1 (`/opt/spark`).
- 🔌 **Tools**: SBT 1.10.7, Maven 3.8.7, IntelliJ IDEA 24.1.
- ☁️ **AWS**: Free Tier account (40 days remaining as of 13/03/2025).
- 😼 **GitHub**: Existing account.

***

## Project Setup and Workflow ⚙️🛠️.

### Step 1: Initialize GitHub 😺 Repository.

Create a GitHub 😺 repository to version control the project.

1. Go to GitHub and create a new repository: <code>x-sentiment-spark-free</code>.
2. Clone it locally:

```
$ git clone https://github.com/<your-username>/x-sentiment-spark-free.git
$ cd x-sentiment-spark-free
```

3. Copy the initial structure from this README (or provided files) into the repo:

- <code>src/main/scala/SentimentAnalysis.scala</code>
- <code>build.sbt</code>
- <code>script/setup_spark.sh</code>
- <code>PROGRESS.md</code>

4. Commit and push:

```
$ git add .
$ git commit -m "Initial project structure"
$ git push origin main
```

**Checkpoint**: Verify the repo exists on GitHub 😺 with all files.

### Step 2: Configure AWS S3 ☁️.

Set up S3 buckets 🪣 for input data and output results within the 5 GB free tier.

1. Install AWS CLI (if not already installed):

```
$ aws --version
# en caso de no estar instalado
$ sudo apt install awscli
$ aws configure  # Add your Access Key, Secret Key, region (e.g., us-east-1)
```

🔑 **Obten tu Access Key y Secret Key**

2. **Inicia sesión en AWS**

- Ve a AWS Management Console con tu cuenta actual.

3. **Accede a IAM (Identity and Access Management)**:

- Generar credenciales y asignar permisos a <code>User</code>
- Selecciona al usuario o agrega uno. Dirigete a menu <code>Agregar Permisos</code> y elige <code>Adjuntar políticas directamente</code>.
- En el buscador de políticas, escribe y selecciona:
	+ <code>AmazonS3FullAccess</code>: Esto permite leer y escribir en S3, necesario para tu proyecto.
	+ (Opcional)<code>AmazonEC2FullAccess</code>: Si quieres administrar instancias EC2 desde el CLI.
	
![](https://raw.githubusercontent.com/gabrielfernando01/x-sentiment-spark-free/main/image/permissions.png)

4. **Genera un Access Key 🔑 para <code>User</code>**

- En el perfil de <code>usuario</code> ve a la pestaña **"Access key"**.
- Haz clic en **Crear clave de acceso**.
- Selecciona el caso de uso: **Interfaz de línea de comando (CLI)**.

5. Configura <code>aws configure</code> con las credenciales de <code>User</code>.

Ahora que tienes las credenciales, regresa a tu terminal en Kubuntu y ejecuta <code>aws configure</code>.

<code>$ aws configure</code>

+ **Ingresa credenciales**
	+ **AWS Access Key ID**: <code>XXXXXXXXXXXXXX</code>.
	+ **AWS Secret Access Key**: XXXXXXXXXXXX</code>.
	+ **Default region name**: Usa <code>us-east-1</code>, que es común y compatible con la capa gratuita.
	+ **Default output forma**: <code>json</code>.
	
6. Verifica la configuración

Prueba que las credencialers funcionan:

<code>$ aws s3 ls</code>

7. Create input and output buckets 🪣:

```
aws s3 mb s3://x-sentiment-input-username --region us-east-1
aws s3 mb s3://x-sentiment-output-username --region us-east-1
```

**Checkpoint**: Verifica los buckets 🪣:

<code>aws s3 ls</code>

8. Download 📩 a public X dataset (e.g., "Sentiment Analysis Dataset Crowdflower" en Kaggle):

- Example: [US Election 2020 Tweets](https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets)
- Archivo a descargar: Descarga el archivo <code></code> (o similar, dependiendo de la fuente).

8.1 Filtrar el dataset antes de subirlo a S3.

Dado que el dataset (<code>training.1600000.processed.noemoticon.csv</code>) contiene 1.6 millones de tweets y no todos son relevantes para tu análisis (sentimientos sobre "Donald Trump" o "elecciones 2024"), filtrarlo antes de subirlo a S3 es una buena práctica. Esto reduce el tamaño del archivo, optimiza el uso del almacenamiento en S3 y hace que el procesamiento en Spark 💥 sea más eficiente.

**Pasos para filtrar el dataset**

8.1.1 **Verifica el tamaño del dataset**

- Abre el fichero para confirmar su estructura, el formato debe ser el siguiente:

```
"target","ids","date","flag","user","text"
0,1467810369,"Mon Apr 06 22:19:45 PDT 2009","NO_QUERY","user1","I hate mondays"
4,1467810672,"Mon Apr 06 22:19:49 PDT 2009","NO_QUERY","user2","I love this sunny day"
```

- Columnas relevantes: <code>target</code> (sentimiento: 0=negativo, 4=positivo), <code>date</code> (fecha), <code>text</code> (contenido del tweet).

8.1.2 **Filtra el dataset con Python 🐍**

Usa el siguiente script para filtrar los tweets que mencionen "Donald Trump" (o el tema de tu elección, como "elecciones 2024"):

```
import pandas as pd

```

9. Upload the dataset to S3:

```
aws s3 cp posts.csv s3://x-sentiment-input/
```

**Checkpoint**: Run <code>aws s3 ls s3://x-sentiment-input</code>. You should see <code>post.csv</code>.

***

### Step 3: Develop Spark 💥 Code Locally.

Write and test the Scala/Spark 🟥💥 code on your laptop 💻 before deploying to AWS ☁️.

1. Open IntelliJ IDEA 🟧, import the project, and ensure SBT resolves dependencies (<code>build.sbt</code>).
2.  Configure Spark 💥 to access S3 locally:

- Edit <code>$SPARK_HOME/conf/spark-default.conf</code>, si no existe el fichero crealo:

```
spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
spark.hadoop.fs.s3a.aws.credentials.provider=org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider
spark.hadoop.fs.s3a.access.key=<your-access-key>
spark.hadoop.fs.s3a.secret.key=<your-secret-key>
```

3. Test with a small sample localy:

- Create a <code>sample.csv</code> (e.g., 10 rows from <code>post.csv</code>).
- Run <code>SentimentAnalysis.scala</code> with:

```
/opt/spark/bin/spark-submit --class SentimentAnalysis --master local[2] target/scala-2.13/x-sentiment-spark_2.13-1.0.jar
```

**Checkpoint**: Check the console for output (e.g., sentiments counts). Fix errors if any.

***

### Step 4: Launch 🚀 EC2 Instance.

Deploy Spark 💥 on an EC2 <code>t2.micro</code> instance within the 750-hour free tier.

1. Create an IAM Role for EC2:
	- Go to IAM > Roles > Create role.
	- Select "AWS service" > "EC2"
	- Attach 'AmazonS3FullAccess' policy.
	- Name it 'EC2-S3-Role' and create.

2. Launch 🚀 a <code>t2.micro</code> instance with the IAM role:

```
$ aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --key-name <your-key> --iam-instance-profile Name:EC2-S3-Role --region us-east-1
```

- Note the instance ID (e.g., <code>i-1234567890abcdef0</code>).

2. Connect via SSH:

```
ssh -i <your-key.pem> ubuntu@<instance-public-ip>
```

3. Install dependencies on EC2:

```
sudo apt update
sudo apt install openjdk-11-jdk git
wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar xvf spark-3.5.1-bin-hadoop3.tgz
sudo mv spark-3.5.1-bin-hadoop3 /opt/spark
echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin" >> ~/.bashrc
source ~/.bashrc
```

4. Clone the repo and configure Spark for S3 (using IAM role):

```
$ git clone https://github.com/<your-username>/x-sentiment-spark-free.git
$ cd x-sentiment-spark-free
$ nvim /opt/spark/conf/spark-default.conf
```

Add:

```
spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
spark.hadoop.fs.s3a.aws.credentials.provider=com.amazonaws.auth.InstanceProfileCredentialsProvider
```

En el README anterior pedia hacer lo siguiente:

```cp scripts/setup_spark.sh .
bash setup_spark.sh  # Add AWS credentials to spark-defaults.conf
```

**Checkpoint**: Run <code>/opt/spark/bin/spark-submit --version</code>. You should see Spark 3.5.1

***

### Step 5: Execute Spark 💥 Job on EC2.

Run the sentiment analysis job and store result in S3.

1. Compile the code locally with SBT:

<code>sbt package</code>

2. Upload the JAR to EC2:

```
scp -i <your-key.pem> target/scala-2.13/x-sentiment-spark_2.13-1.0.jar ubuntu@<instance-ip>:~/x-sentiment-spark-free/
```

3. Run the job on EC2:

```
aws ec2 stop-instances --instance-id i-1234567890abcdef0
```

4. Stop 🚦 the instance after execution to save hours:

```
aws ec2 stop-instances --instance-id i-1234567890abcdef0
```

**Checkpoint**: Check <code>s3://x-sentiment-output/result/</code> with <code>aws s3 ls</code>. You should see Paruquet files partitioned by date.

***

### Step 6. Validate and Migrate (in 40 Days).

After 40 days, migrate to a new AWS Free Tier account.

1. Download resutls locally:

```
aws s3 sync s3://x-sentiment-output/ ./results/
```

2. Create a new AWS account and configure new buckets.
3. Upload data and results:

```
aws s3 cp posts.csv s3://x-sentiment-input-new/
aws s3 sync ./results/ s3://x-sentiment-output-new/
```

**Checkpoint**: Verify new buckets with <code>aws s3 ls</code>.

****

### Troubleshooting 💡.

- **S3 Access Denied**: Check AWS credentials in <code>spark-default.conf</code>.
- **OutOfMemoryError**: Reduce dataset size or adjust <code>spark.executor.memory</code> (e.g., 512m),
- **EC2 Hours Exceeded**: Monitor usage with <code>aws ec2 describe-instances</code>.

***

### Progress Tracking 📋.

Update <code>docs/PROGRESS.md</code> after each step:

```
- [ ] Step 1: GitHub repo created
- [ ] Step 2: S3 buckets configured
- [ ] Step 3: Code tested locally
- [ ] Step 4: EC2 instance launched
- [ ] Step 5: Job executed
- [ ] Step 6: Migration completed
```

***

### Next Steps

Start with Step 1. After each step, commit changes to GitHub and update PROGRESS.md. Resume by telling Grok your last completed step.

```
---

### Resumen (13/03/2025)
```

- Objetivo: Análisis de sentimientos en posts de X, conteo diario, resultados en S3 (capa gratuita).
- Recursos: 16 GB RAM, Kubuntu, Spark 3.5.1, Scala 2.13.8, AWS (40 días restantes).
- Diseño: Spark en EC2 t2.micro, S3 buckets, GitHub repo <code>x-sentiment-spark-free</code>.
- README.md: Guía detallada entregada.
- Próximos pasos:

	1. Crear el repo <code>x-sentiment-spark-free</code> y sube la escritura.
	2. Configurar buckets S3 y sube un dataset (1-2 GB).
	3. Prueba el código localmente. Guarda este resumen y dime la próxima sesión qué completaste.
	
```
---
### Detalles adicionales como ingeniero de datos
- **Optimización**: El código usa particiones por fecha en S3 (`partitionBy("date")`) para eficiencia en consultas futuras.
- **Escalabilidad**: Aunque limitado a `t2.micro`, el diseño es portable a EMR si decides invertir más tarde.
- **Dataflow**: El flujo S3 → Spark → S3 sigue mejores prácticas de ETL en big data.

¿Listo para arrancar? Crea el repo y sigue el `README.md`. Si necesitas ayuda con el dataset o el paso 1, ¡avísame!
```