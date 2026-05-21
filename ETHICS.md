# Ética, sesgos y transparencia del modelo

Este documento resume los principales riesgos éticos, posibles sesgos y limitaciones del proyecto de predicción de abandono de clientes (*Customer Churn*) usando el dataset **Telco Customer Churn**. Su objetivo es dejar claro qué puede y qué no puede inferirse a partir del modelo, así como establecer buenas prácticas mínimas para su uso responsable.

## 1. Contexto del proyecto

El modelo busca predecir si una persona cliente de una empresa de telecomunicaciones podría abandonar el servicio. Este proyecto tiene fines educativos y de práctica de MLOps, por lo que sus resultados no deben utilizarse directamente para tomar decisiones reales sobre clientes sin una validación adicional, monitoreo de desempeño y revisión ética-operativa.

La variable objetivo es `Churn`, que indica si el cliente abandonó o no el servicio. El modelo utiliza variables contractuales, de servicio y facturación, como tipo de contrato, servicios contratados, método de pago, permanencia, cargos mensuales y cargos totales.

## 2. Variables sensibles o potencialmente sensibles

El dataset incluye algunas variables que pueden relacionarse directa o indirectamente con características personales o condiciones de vulnerabilidad. Entre ellas:

- `gender`: puede introducir diferencias de trato por género si el modelo aprende patrones no justificados.
- `SeniorCitizen`: identifica si la persona es adulta mayor, lo que puede representar un grupo con necesidades, hábitos de consumo o condiciones económicas distintas.
- `Partner` y `Dependents`: reflejan composición familiar o del hogar, información que puede tener implicaciones sociales y económicas.
- `PaymentMethod`, `MonthlyCharges` y `TotalCharges`: no son variables sensibles por sí mismas, pero pueden funcionar como aproximaciones indirectas de capacidad económica o estabilidad financiera.

Aunque el dataset no incluye variables como raza, etnia, religión, discapacidad, código postal o ingreso explícito, sí existen variables que podrían generar efectos diferenciados entre grupos de clientes.

## 3. Posibles sesgos del dataset

El modelo depende de los datos históricos disponibles. Si esos datos reflejan prácticas comerciales previas, desigualdades de acceso, diferencias socioeconómicas o patrones de atención diferenciada, el modelo puede reproducir esos sesgos.

Algunos riesgos posibles son:

- **Subrepresentación:** algunos grupos pueden estar poco representados en el dataset, lo que reduce la capacidad del modelo para predecir correctamente sobre ellos.
- **Sesgo histórico:** las etiquetas de abandono pueden reflejar condiciones pasadas de servicio, precios, atención al cliente o estrategias comerciales que no necesariamente deberían repetirse.
- **Sesgo por variables proxy:** variables como método de pago, cargos mensuales o tipo de contrato pueden estar asociadas indirectamente con nivel socioeconómico u otras condiciones personales.
- **Desbalance de clases:** si hay muchos más casos de clientes que no abandonan el servicio que casos de abandono, el modelo puede aparentar buen desempeño general, pero fallar al identificar correctamente los casos de `Churn`.

## 4. Limitaciones del modelo

Este modelo no explica por sí mismo las causas del abandono. Una predicción de `Churn` indica probabilidad o clasificación estimada, pero no demuestra que una variable específica sea la causa de que una persona abandone el servicio.

También debe considerarse que:

- El desempeño puede cambiar si se usa con datos nuevos o de otra empresa.
- Las métricas globales como `accuracy` pueden ser insuficientes si no se revisan también `recall`, `precision`, `f1-score` y matriz de confusión.
- El modelo puede fallar más en ciertos grupos de clientes si no se evalúa el desempeño por segmentos relevantes.
- Las predicciones no deben sustituir el juicio humano ni la revisión de contexto comercial y de atención al cliente.

## 5. Uso responsable recomendado

Si este proyecto se adaptara a un contexto real, se recomienda:

1. Evaluar el desempeño por segmentos, por ejemplo, género, personas adultas mayores, tipo de contrato y método de pago.
2. Revisar métricas enfocadas en `Churn`, especialmente `recall`, porque en este problema puede ser más importante detectar a quienes sí podrían abandonar el servicio.
3. Evitar decisiones perjudiciales para clientes con base únicamente en la predicción del modelo.
4. Usar el modelo para mejorar la atención, ofrecer soporte o identificar necesidades, no para discriminar, excluir o aumentar precios a grupos específicos.
5. Documentar los datos usados, las transformaciones realizadas y la versión del modelo entrenado.
6. Monitorear periódicamente si el desempeño baja o si aparecen errores sistemáticos en algún grupo.

## 6. Transparencia

Toda ejecución del pipeline debería documentar:

- Fecha de entrenamiento.
- Dataset usado.
- Parámetros definidos en `config/params.yaml`.
- Algoritmo seleccionado.
- Métricas obtenidas.
- Ruta del modelo guardado.

Esto ayuda a que el proyecto sea reproducible y facilita detectar errores, cambios de comportamiento o problemas de sesgo.

## 7. Conclusión

El modelo puede ser útil como ejercicio técnico para aprender integración de datos, entrenamiento, evaluación y despliegue básico. Sin embargo, sus predicciones deben interpretarse con cuidado. En un entorno real, el objetivo ético debería ser mejorar la experiencia del cliente y prevenir abandono mediante atención justa, no automatizar decisiones que puedan producir trato desigual o injustificado.
