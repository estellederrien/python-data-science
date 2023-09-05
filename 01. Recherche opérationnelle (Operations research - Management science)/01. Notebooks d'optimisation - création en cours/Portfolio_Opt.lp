\* Portfolio_Opt *\
Minimize
OBJ: 40 Potential_Investment_Antony_Hotels
 + 30 Potential_Investment_Arkansas_REIT
 + 25 Potential_Investment_Atlantic_Lightning
 + 20 Potential_Investment_Bedrock_Insurance_Annuity
 + 65 Potential_Investment_Minocompo_System
 + 15 Potential_Investment_Nocal_Mining_Bond
Subject To
Investments: Potential_Investment_Antony_Hotels
 + Potential_Investment_Arkansas_REIT
 + Potential_Investment_Atlantic_Lightning
 + Potential_Investment_Bedrock_Insurance_Annuity
 + Potential_Investment_Certificate_of_deposit
 + Potential_Investment_Minocompo_System
 + Potential_Investment_Nocal_Mining_Bond
 + Potential_Investment_Saving_Account = 100000
Liquidity: Potential_Investment_Antony_Hotels
 + Potential_Investment_Arkansas_REIT
 + Potential_Investment_Atlantic_Lightning
 + Potential_Investment_Minocompo_System + Potential_Investment_Saving_Account
 >= 40000
Ratings: Potential_Investment_Bedrock_Insurance_Annuity
 + Potential_Investment_Certificate_of_deposit
 + Potential_Investment_Minocompo_System + Potential_Investment_Saving_Account
 >= 50000
Returns: 0.125 Potential_Investment_Antony_Hotels
 + 0.1 Potential_Investment_Arkansas_REIT
 + 0.071 Potential_Investment_Atlantic_Lightning
 + 0.082 Potential_Investment_Bedrock_Insurance_Annuity
 + 0.052 Potential_Investment_Certificate_of_deposit
 + 0.2 Potential_Investment_Minocompo_System
 + 0.065 Potential_Investment_Nocal_Mining_Bond
 + 0.04 Potential_Investment_Saving_Account >= 7500
Save_and_CD: Potential_Investment_Certificate_of_deposit
 + Potential_Investment_Saving_Account <= 30000
End
