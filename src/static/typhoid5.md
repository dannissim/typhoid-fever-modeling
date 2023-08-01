### My Model
The question that interested me and the one that I chose to focus on is somewhat different than
what the model in the research paper takes into account. What I wanted to find out is how improving
sanitation with efforts like Gram Vikas can impact the dynamics Typhoid, and what is required in 
order to eradicate the disease. To do this I created my own model that is inspired by the model
shown in the paper, parameters I kept from their model are: 
the estimated basic reproductive number R0 of ~2.5, the recovery rate of 0.25 per time period 
and a transmission rate of 0.625, 
the rate of infected that become chronic carriers θ, the relative infectiousness of chronic carriers
of 0.01. The important addition to my model is the introduction of a sanitation improvement factor λ
which will lower the transmission rate β every time period. So for example for λ = 1%, and β = 0.5,
then after a week the new β will be 0.5 * 99% = 0.45, and the next week 0.45 * 99% and so on.
This should capture the effect of intervention. Our goal will be to see if such a λ exists to 
eradicate Typhoid or at least come very close to eradication.

### Interactive App
Welcome to our interactive SIR model app! Here, you can explore and simulate the fascinating 
transmission dynamics of typhoid fever. Using sliders, you have the power to adjust various 
parameters of the model, allowing you to observe how changes in factors like transmission rate, 
recovery rate, and initial population affect the progression of the disease. Gain insights into how
infectious diseases spread and evolve over time. Have fun experimenting with different scenarios
and unraveling the complexities of typhoid fever dynamics. Enjoy!