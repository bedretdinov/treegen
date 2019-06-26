# treegen

the module for generate if else tree for intergation your model to mysql or php


### for install 
```sh 
  pip3 install git+https://github.com/bedretdinov/treegen 
```


### generate SQL
```python
from treegen import TreeGenerator
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
  
iris.feature_names = ['sepal_length_sm','sepal_width_sm','petal_length_sm','petal_width_sm']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)


TreeGenerator.toSQL(clf, iris.feature_names)


```

### result SQL
 
```sql 
if(petal_width_sm <= 0.800000011920929, 0  , if(petal_width_sm <= 1.75,if(petal_length_sm <= 4.950000047683716,if(petal_width_sm <= 1.6500000357627869, 1  ,  2   ), if(petal_width_sm <= 1.550000011920929, 2  , if(petal_length_sm <= 5.450000047683716, 1  ,  2   ) ) ), if(petal_length_sm <= 4.8500001430511475,if(sepal_width_sm <= 3.100000023841858, 2  ,  1   ),  2   ) ) )
```


### generate PHP
```python
from treegen import TreeGenerator
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
  
iris.feature_names = ['sepal_length_sm','sepal_width_sm','petal_length_sm','petal_width_sm']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)


TreeGenerator.toPHP(clf, iris.feature_names) 
```

### result PHP


```php 
  if(petal_length_sm <= 2.449999988079071){
      return 0 
   }else{  
    if(petal_width_sm <= 1.75){
      if(petal_length_sm <= 4.950000047683716){
        if(petal_width_sm <= 1.6500000357627869){
            return 1 
         }else{  
            return 2 
        }
       }else{  
        if(petal_width_sm <= 1.550000011920929){
            return 2 
         }else{  
          if(petal_length_sm <= 5.450000047683716){
              return 1 
           }else{  
              return 2 
          }
        }
      }
     }else{  
      if(petal_length_sm <= 4.8500001430511475){
        if(sepal_width_sm <= 3.100000023841858){
            return 2 
         }else{  
            return 1 
        }
       }else{  
          return 2 
      }
    }
  }
```