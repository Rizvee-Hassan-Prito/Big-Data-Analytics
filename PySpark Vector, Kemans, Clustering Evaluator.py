#PySpark Vector, Kemans, Clustering Evaluator

data_customer=spark.read.csv('CC GENERAL.csv',header=True, inferSchema=True)

data_customer.printSchema()

data_customer=data_customer.na.drop()

print(data_customer.columns)

from pyspark.ml.feature import VectorAssembler

assemble=VectorAssembler(inputCols=['BALANCE','BALANCE_FREQUENCY','PURCHASES','ONEOFF_PURCHASES','CASH_ADVANCE','PURCHASES_FREQUENCY','ONEOFF_PURCHASES_FREQUENCY','PURCHASES_INSTALLMENTS_FREQUENCY','CASH_ADVANCE_FREQUENCY','CASH_ADVANCE_TRX','PURCHASES_TRX','CREDIT_LIMIT','PAYMENTS','MINIMUM_PAYMENTS','PRC_FULL_PAYMENT','TENURE'],outputCol='features')
assembled_data=assemble.transform(data_customer)
assembled_data.show(5)

from pyspark.ml.feature import StandardScaler

scale=StandardScaler(inputCol='features',outputCol='standardized')

data_scale=scale.fit(assembled_data)
data_scale_output=data_scale.transform(assembled_data)

data_scale_output.show(5)


from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

silhouette_score=[]

evaluator=ClusteringEvaluator(predictionCol='prediction',featuresCol='standardized',metricName='silhouette', distanceMeasure='squaredEuclidean')

for i in range(2,10):
  KMeans_algo=KMeans(featuresCol='standardized',k=i)

  KMeans_fit=KMeans_algo.fit(data_scale_output)

  output=KMeans_fit.transform(data_scale_output)
  score= evaluator.evaluate(output)

  silhouette_score.append(score)

  print("Silhouette Score for k=",i,"-->",score)

print(silhouette_score)

#visualizing the silhoutte scores in a plot
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,1,figsize=(8,6))
ax.plot(range(2,10),silhouette_score)
ax.set_xlabel('k')
ax.set_ylabel('cost')