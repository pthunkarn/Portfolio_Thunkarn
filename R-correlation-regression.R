## Correlation
cor(mtcars$hp, mtcars$mpg)
plot(mtcars$hp, mtcars$mpg, pch=16)

cor(mtcars[ , c("mpg", "wt", "hp")]) ##[rows, columns]

## dplyr (tidyverse)
library(dplyr)

corMat <- mtcars %>%
  select(mpg, wt, hp) %>%
  cor()

## compute correlation (r) and sig test
cor(mtcars$hp, mtcars$mpg)
cor.test(mtcars$hp, mtcars$mpg)

## Linear regression
## mpg = f(hp)

lmfit <- lm(mpg~hp, data = mtcars)
summary(lmfit)

## prediction
lmfit$coefficients[[1]] + lmfit$coefficients[[2]]*200

new_cars <- data.frame(
  hp = c(250, 320, 400, 410, 450)
)

## predict ()
new_cars$mpg_pred <- predict(lmfit, newdata = new_cars)
new_cars

## Root Mean Square Error (rmse)
## Multiple Linear Regression
## mpg = f(hp, wt, am)
## mpg = intercept +b0*hp +b1*wt +b2*am

lmfit_v2 <- lm(mpg~hp+wt+am, data = mtcars)

mtcars$predicted <- predict(lmfit_v2)
squared_error <- (mtcars$predicted - mtcars$mpg) ** 2
mean_squared_error <- mean(squared_error)
rmse <- sqrt(mean_squared_error)
rmse

## Build Full Model
lmfit_full <- lm(mpg ~ . -gear, data = mtcars)

## Split Data
set.seed(42)
n <- nrow(mtcars)
id <- sample(1:n, size=n*0.8)
train_data <- mtcars[id, ]
test_data <- mtcars[-id, ]

## Train Model
model1 <- lm(mpg~hp+wt, data = train_data)
p_train <- predict(model1)
error_train <- train_data$mpg - p_train
rmse_train <- sqrt(mean(error_train**2))
rmse_train

## Test Model
p_test <- predict(model1, newdata = test_data)
error_test <- test_data$mpg - p_test
rmse_test <- sqrt(mean(error_test**2))
rmse_test

## Print Result
cat("RMSE Train", rmse_train, 
    "\nRMSE Test", rmse_test)














