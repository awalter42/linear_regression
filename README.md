Linear regression
======================
A simple linear regression model to predict a car's price depending on it's mileage

Usage
======================
if you want to see the graphs `export QT_QPA_PLATFORM=wayland`

```bash
python3 main.py
```
You can then follow the prompt to use the program

If the model is saved you can then use `python3 predict.py` to predict values, the data file is the same as the one used for training, it is used to get the normalization datas

If no model was saved, the default values (0,0) will be used for predictions
