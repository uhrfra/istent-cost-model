# iStent Cost Model - Abstract


## Purpose

Estimation of the efficacy and costs of combined phacoemulsification and iStent inject
trabecular bypass implant in mild-to-moderate open angle glaucoma in a real-world setting in
Germany.

## Methods

96 eyes of 96 patients (49% male) were included in our interventional case series.
Diagnoses included primary open angle glaucoma, pseudoexfoliative glaucoma and pigmentary
glaucoma. Efficacy outcomes were intraocular pressure (IOP) and glaucoma medication reduction 4
weeks after surgery. To estimate costs, an individual patient sampling model was set up in Python
3.11 programming language to simulate patients in a Monte-Carlo approach over their lifetime. Age,
mortality rate and medications were implemented at a cycle length of 0,33 years in a 2-state Markov
model. Direct costs and cost savings due to discontinuation of glaucoma medication were recorded
and compared to standard of care.

## Results

Mean IOP was reduced from 18,7 (SD 4,2) mmHg to 14,6 (SD 3,0) mmHg. Topical glaucoma
medications were reduced in 48 patients and completely discontinued in 33 patients. Mean
medications were reduced from 2,23 (SD 1,12) to 1,42 (SD 1,34). Direct costs of the iStent inject
procedure were €1288,81 including value-added tax. In our model, total direct costs accrued to
€4265,47 for the iStent inject procedure vs. €5164,62 for standard of care over a patient’s lifetime.
Sensitivity analysis showed the model’s robustness.

## Conclusion

iStent inject combined with phacoemulsification reduces both IOP and glaucoma
medication and profs to be an effective way of managing mild-to-moderate open angle glaucoma.
Despite high initial costs, the procedure can lower treatment costs from a patient’s lifetime
perspective.
