import math

# Sigmoide è una funzione di attivazione comunemente usata nelle reti neurali. La sua formula è:
def sigomoide(z):
    return 1 / (1 + math.exp(-z))

print(sigomoide(1))

# ReLU (Rectified Linear Unit) è un'altra funzione di attivazione molto popolare nelle reti neurali, soprattutto nelle reti profonde. La sua formula è:
def rectified_linear_unit(z):
    return max(0, z)

print(rectified_linear_unit(-1))
print(rectified_linear_unit(1))


# Tanh (tangente iperbolica) è una funzione di attivazione che mappa i valori in un intervallo compreso tra -1 e 1. La sua formula è:
def tanh(z):
    return (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))

print(tanh(1))

# Log Loss è una funzione di perdita comunemente usata nelle reti neurali per problemi di classificazione. La sua formula è:
def log_loss(y_true, y_pred):
    loss = 0

    for yt, yp in zip(y_true, y_pred):
        loss += -yt * math.log(yp) - (1 - yt) * math.log(1 - yp)

    return loss

print(log_loss([1, 0, 1, 1, 0], [0.9, 0.1, 0.8, 0.7, 0.2]))