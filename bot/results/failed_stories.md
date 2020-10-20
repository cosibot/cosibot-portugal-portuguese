## pt_covid_situation_without_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: Como está a situação em Ucrânia?   <!-- predicted: pt_covid_situation: Como está a situação em [Ucrânia]{"entity": "pt_country_code", "value": "UA"}[Ucrânia]{"entity": "pt_country_code", "value": "UA"}? -->
    - slot{"pt_country_code": "UA"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sem dúvida
    - utter_pt_ask_which_country
* pt_country: Guyane   <!-- predicted: pt_country: [Guyane]{"entity": "pt_country_code", "value": "GF"}[Guyane]{"entity": "pt_country_code", "value": "GF"} -->
    - slot{"pt_country_code": "GF"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Estados Unidos da América"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation


## covid_situation_without_country2 (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: Quantos mortos houve em portugal hoje?   <!-- predicted: pt_covid_situation: Quantos mortos houve em [portugal]{"entity": "pt_country_code", "value": "PT"}[portugal]{"entity": "pt_country_code", "value": "PT"} hoje? -->
    - slot{"pt_country_code": "PT"}
    - utter_pt_want_to_add_country
* pt_vocative_no: certamente que não
    - utter_pt_further_questions


## covid_situation_without_country3 (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: Estatísticas actualizadas em Singapura   <!-- predicted: pt_covid_situation: Estatísticas actualizadas em [Singapura]{"entity": "pt_country_code", "value": "SG"}[Singapura]{"entity": "pt_country_code", "value": "SG"} -->
    - slot{"pt_country_code": "SG"}
    - utter_pt_want_to_add_country
* pt_country: Guyane   <!-- predicted: pt_country: [Guyane]{"entity": "pt_country_code", "value": "GF"}[Guyane]{"entity": "pt_country_code", "value": "GF"} -->
    - slot{"pt_country_code": "GF"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Espanha"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation


## pt_covid_situation_happy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: Quantos infectados existem neste momento em Região de Lisboa   <!-- predicted: pt_covid_situation: Quantos infectados existem neste momento em [Região de Lisboa]{"entity": "pt_country_region", "value": "Lisboa"}[Região de Lisboa]{"entity": "pt_country_region", "value": "Lisboa"} -->
    - slot{"pt_country_region": "Lisboa"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Itália"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation   <!-- predicted: action_default_fallback -->


## pt_covid_situation_unhappy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: quantos mortos em portugal?   <!-- predicted: pt_covid_situation: quantos mortos em [portugal]{"entity": "pt_country_code", "value": "PT"}[portugal]{"entity": "pt_country_code", "value": "PT"}? -->
    - slot{"pt_country_code": "PT"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_unhappy_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: numeros para Região Norte hoje   <!-- predicted: pt_covid_situation: numeros para [Região Norte]{"entity": "pt_country_region", "value": "Norte"}[Região Norte]{"entity": "pt_country_region", "value": "Norte"} hoje -->
    - slot{"pt_country_region": "Norte"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: Uhum.
    - utter_pt_ask_which_country
* pt_country: Andorra   <!-- predicted: pt_country: [Andorra]{"entity": "pt_country_code", "value": "AD"}[Andorra]{"entity": "pt_country_code", "value": "AD"} -->
    - slot{"pt_country_code": "AD"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation   <!-- predicted: action_default_fallback -->


## pt_covid_situation_unhappy_inexistent_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: Quantos casos existem em Murça?   <!-- predicted: pt_covid_situation: Quantos casos existem em [Murça](pt_country_municipal)[Murça](pt_country_municipal)? -->
    - slot{"pt_country_municipal": "Murça"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: totalmente
    - utter_pt_ask_which_country
* pt_country: Costa Rica   <!-- predicted: pt_country: [Costa Rica]{"entity": "pt_country_code", "value": "CR"}[Costa Rica]{"entity": "pt_country_code", "value": "CR"} -->
    - slot{"pt_country_code": "CR"}
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_unhappy_with_dashboard (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: Quantos casos existem em Évora?   <!-- predicted: pt_covid_situation: Quantos casos existem em [Évora](pt_country_municipal)[Évora](pt_country_municipal)? -->
    - slot{"pt_country_municipal": "Évora"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: nunca, de todo
    - utter_pt_covid_current_statistics


## pt_covid_situation_deaths_happy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_deaths: Mortes em República do Uzbequistão   <!-- predicted: pt_covid_situation_deaths: Mortes em [República do Uzbequistão]{"entity": "pt_country_code", "value": "UZ"}[República do Uzbequistão]{"entity": "pt_country_code", "value": "UZ"} -->
    - slot{"pt_country_code": "UZ"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Suécia"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_deaths


## pt_covid_situation_deaths_unhappy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_deaths: Qual é o número de mortos em República de Guinea Ecuatorial?   <!-- predicted: pt_covid_situation_deaths: Qual é o número de mortos em [República de Guinea Ecuatorial]{"entity": "pt_country_code", "value": "GQ"}[República de Guinea Ecuatorial]{"entity": "pt_country_code", "value": "GQ"}? -->
    - slot{"pt_country_code": "GQ"}
    - action_search_stats
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_deaths_unhappy_general_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_deaths: Número total de mortos em Malawi?   <!-- predicted: pt_covid_situation_deaths: Número total de mortos em [Malawi]{"entity": "pt_country_code", "value": "MW"}[Malawi]{"entity": "pt_country_code", "value": "MW"}? -->
    - slot{"pt_country_code": "MW"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: yep
    - utter_pt_ask_which_country
* pt_country: Bulgária   <!-- predicted: pt_country: [Bulgária]{"entity": "pt_country_code", "value": "BG"}[Bulgária]{"entity": "pt_country_code", "value": "BG"} -->
    - slot{"pt_country_code": "BG"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Suécia"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_deaths


## pt_covid_situation_deaths_unhappy_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_deaths: Qual é o número de mortos em República de Guinea Ecuatorial?   <!-- predicted: pt_covid_situation_deaths: Qual é o número de mortos em [República de Guinea Ecuatorial]{"entity": "pt_country_code", "value": "GQ"}[República de Guinea Ecuatorial]{"entity": "pt_country_code", "value": "GQ"}? -->
    - slot{"pt_country_code": "GQ"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: está certo
    - utter_pt_ask_which_country
* pt_country: Tanzania   <!-- predicted: pt_country: [Tanzania]{"entity": "pt_country_code", "value": "TZ"}[Tanzania]{"entity": "pt_country_code", "value": "TZ"} -->
    - slot{"pt_country_code": "TZ"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Suécia"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_deaths


## pt_covid_situation_deaths_unhappy_inexistent_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_deaths: República Federal da Alemã mortes.   <!-- predicted: pt_covid_situation_deaths: [República Federal da Alemã]{"entity": "pt_country_code", "value": "DE"}[República Federal da Alemã]{"entity": "pt_country_code", "value": "DE"} mortes. -->
    - slot{"pt_country_code": "DE"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim sim
    - utter_pt_ask_which_country
* pt_country: Myanmar   <!-- predicted: pt_country: [Myanmar]{"entity": "pt_country_code", "value": "MM"}[Myanmar]{"entity": "pt_country_code", "value": "MM"} -->
    - slot{"pt_country_code": "MM"}
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_deaths_unhappy_with_dashboard (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_deaths: Quantos mortos existem neste momento em HIMI?   <!-- predicted: pt_covid_situation_deaths: Quantos mortos existem neste momento em [HIMI]{"entity": "pt_country_code", "value": "HM"}[HIMI]{"entity": "pt_country_code", "value": "HM"}? -->
    - slot{"pt_country_code": "HM"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: de jeito nenhum
    - utter_pt_covid_current_statistics


## pt_covid_situation_infected_happy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Contagem infectados no total em Calheta (São Jorge){"entity": "pt_country_municipal", "value": "Calheta (São Jorge)"}   <!-- predicted: pt_covid_situation_infected: Contagem infectados no total em [Calheta (São Jorge){"entity](pt_country_municipal)": "pt_country_municipal", "[value": "Calheta (São Jorge](pt_country_municipal))"} -->
    - slot{"pt_country_municipal": "value\": \"Calheta (São Jorge"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Itália"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_infected


## pt_covid_situation_infected_unhappy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: quantos casos há em Reino da Jordânia no momento?   <!-- predicted: pt_covid_situation_infected: quantos casos há em [Reino da Jordânia]{"entity": "pt_country_code", "value": "JO"}[Reino da Jordânia]{"entity": "pt_country_code", "value": "JO"} no momento? -->
    - slot{"pt_country_code": "JO"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_infected_unhappy_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Casos confirmados em Região Autónoma dos Açores   <!-- predicted: pt_covid_situation_infected: Casos confirmados em [Região Autónoma dos Açores]{"entity": "pt_country_region", "value": "A\u00e7ores"}[Região Autónoma dos Açores]{"entity": "pt_country_region", "value": "A\u00e7ores"} -->
    - slot{"pt_country_region": "Açores"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: Sim, por favor
    - utter_pt_ask_which_country
* pt_country: Canadá   <!-- predicted: pt_country: [Canadá]{"entity": "pt_country_code", "value": "CA"}[Canadá]{"entity": "pt_country_code", "value": "CA"} -->
    - slot{"pt_country_code": "CA"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Itália"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_infected


## pt_covid_situation_infected_unhappy_inexistent_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Número de infectados ativos em Northern Ireland.   <!-- predicted: pt_covid_situation_infected: Número de infectados ativos em [Northern Ireland]{"entity": "pt_country_code", "value": "GB"}[Northern Ireland]{"entity": "pt_country_code", "value": "GB"}. -->
    - slot{"pt_country_code": "GB"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: yep
    - utter_pt_ask_which_country
* pt_country: São Marino   <!-- predicted: pt_country: [São Marino]{"entity": "pt_country_code", "value": "SM"}[São Marino]{"entity": "pt_country_code", "value": "SM"} -->
    - slot{"pt_country_code": "SM"}
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_infected_unhappy_with_dashboard (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Qual é o número de casos confirmados em Seixal   <!-- predicted: pt_covid_situation_infected: Qual é o número de casos confirmados em [Seixal](pt_country_municipal)[Seixal](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Seixal"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: Provavelmente não.
    - utter_pt_covid_current_statistics


## pt_covid_situation_infected_critical_happy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected_critical: Contagem infectada crítica em Bonaire, Sint Eustatius and Saba   <!-- predicted: pt_covid_situation_infected_critical: Contagem infectada crítica em [Bonaire, Sint Eustatius and Saba]{"entity": "pt_country_code", "value": "BQ"}[Bonaire, Sint Eustatius and Saba]{"entity": "pt_country_code", "value": "BQ"} -->
    - slot{"pt_country_code": "BQ"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Espanha"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_infected_critical


## pt_covid_situation_infected_critical_unhappy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected_critical: Contagem infectados graves no South Korea   <!-- predicted: pt_covid_situation_infected_critical: Contagem infectados graves no [South Korea]{"entity": "pt_country_code", "value": "KR"}[South Korea]{"entity": "pt_country_code", "value": "KR"} -->
    - slot{"pt_country_code": "KR"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_infected_critical_unhappy_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected_critical: Contagem infectados alarmantes em República dos Camarões   <!-- predicted: pt_covid_situation_infected_critical: Contagem infectados alarmantes em [República dos Camarões]{"entity": "pt_country_code", "value": "CM"}[República dos Camarões]{"entity": "pt_country_code", "value": "CM"} -->
    - slot{"pt_country_code": "CM"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: naturalmente
    - utter_pt_ask_which_country
* pt_country: Burquina   <!-- predicted: pt_country: [Burquina]{"entity": "pt_country_code", "value": "BF"}[Burquina]{"entity": "pt_country_code", "value": "BF"} -->
    - slot{"pt_country_code": "BF"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Espanha"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_infected_critical


## pt_covid_situation_infected_critical_unhappy_inexistent_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected_critical: Número de infectados graves em Luxemburgo.   <!-- predicted: pt_covid_situation_infected_critical: Número de infectados graves em [Luxemburgo]{"entity": "pt_country_code", "value": "LU"}[Luxemburgo]{"entity": "pt_country_code", "value": "LU"}. -->
    - slot{"pt_country_code": "LU"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: Certo.
    - utter_pt_ask_which_country
* pt_country: no Zimbabué   <!-- predicted: pt_country: no [Zimbabué]{"entity": "pt_country_code", "value": "ZW"}[Zimbabué]{"entity": "pt_country_code", "value": "ZW"} -->
    - slot{"pt_country_code": "ZW"}
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_infected_critical_unhappy_with_dashboard (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected_critical: Número de casos criticos em São Vicente e Granadinas   <!-- predicted: pt_covid_situation_infected_critical: Número de casos criticos em [São Vicente e Granadinas]{"entity": "pt_country_code", "value": "VC"}[São Vicente e Granadinas]{"entity": "pt_country_code", "value": "VC"} -->
    - slot{"pt_country_code": "VC"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: Claro que não.
    - utter_pt_covid_current_statistics


## pt_covid_situation_last_update_happy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Atualização em Montalegre   <!-- predicted: pt_covid_situation_last_update: Atualização em [Montalegre](pt_country_municipal)[Montalegre](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Montalegre"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Inglaterra"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "14302"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_last_update


## pt_covid_situation_last_update_unhappy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Atualização em Trofa   <!-- predicted: pt_covid_situation_last_update: Atualização em [Trofa](pt_country_municipal)[Trofa](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Trofa"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_last_update_unhappy_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Ultima atualização em República de San Marino   <!-- predicted: pt_covid_situation_last_update: Ultima atualização em [República de San Marino]{"entity": "pt_country_code", "value": "SM"}[República de San Marino]{"entity": "pt_country_code", "value": "SM"} -->
    - slot{"pt_country_code": "SM"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: mesmo na muche
    - utter_pt_ask_which_country
* pt_country: Croacia   <!-- predicted: pt_country: [Croacia]{"entity": "pt_country_code", "value": "HR"}[Croacia]{"entity": "pt_country_code", "value": "HR"} -->
    - slot{"pt_country_code": "HR"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Inglaterra"}
    - slot{"new_cases": "987"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_last_update


## pt_covid_situation_last_update_unhappy_inexistent_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Atualização em Seia   <!-- predicted: pt_covid_situation_last_update: Atualização em [Seia](pt_country_municipal)[Seia](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Seia"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: Sim
    - utter_pt_ask_which_country
* pt_country: Samoa   <!-- predicted: pt_country: [Samoa]{"entity": "pt_country_code", "value": "WS"}[Samoa]{"entity": "pt_country_code", "value": "WS"} -->
    - slot{"pt_country_code": "WS"}
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_last_update_unhappy_with_dashboard (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Atualização em Castelo de Paiva   <!-- predicted: pt_covid_situation_last_update: Atualização em [Castelo de Paiva](pt_country_municipal)[Castelo de Paiva](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Castelo de Paiva"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: negativa
    - utter_pt_covid_current_statistics


## pt_covid_situation_recovered_happy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_recovered: Quantos casos de recuperados há em República da Coreia?   <!-- predicted: pt_covid_situation_recovered: Quantos casos de recuperados há em [República da Coreia]{"entity": "pt_country_code", "value": "KR"}[República da Coreia]{"entity": "pt_country_code", "value": "KR"}? -->
    - slot{"pt_country_code": "KR"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Alemanha"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_recovered


## pt_covid_situation_recovered_unhappy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_recovered: qual o numero de recuperados em Federation of Saint Christopher and Nevis?   <!-- predicted: pt_covid_situation_recovered: qual o numero de recuperados em [Federation of Saint Christopher and Nevis]{"entity": "pt_country_code", "value": "KN"}[Federation of Saint Christopher and Nevis]{"entity": "pt_country_code", "value": "KN"}? -->
    - slot{"pt_country_code": "KN"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_recovered_unhappy_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_recovered: Numero de recuperações em São Marino hoje?   <!-- predicted: pt_covid_situation_recovered: Numero de recuperações em [São Marino]{"entity": "pt_country_code", "value": "SM"}[São Marino]{"entity": "pt_country_code", "value": "SM"} hoje? -->
    - slot{"pt_country_code": "SM"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: mesmo na muche
    - utter_pt_ask_which_country
* pt_country: Aruba   <!-- predicted: pt_country: [Aruba]{"entity": "pt_country_code", "value": "AW"}[Aruba]{"entity": "pt_country_code", "value": "AW"} -->
    - slot{"pt_country_code": "AW"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Alemanha"}
    - slot{"new_cases": "987"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_recovered


## pt_covid_situation_recovered_unhappy_inexistent_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_recovered: Quantos recuperados tem Chad?   <!-- predicted: pt_covid_situation_recovered: Quantos recuperados tem [Chad]{"entity": "pt_country_code", "value": "TD"}[Chad]{"entity": "pt_country_code", "value": "TD"}? -->
    - slot{"pt_country_code": "TD"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: yep
    - utter_pt_ask_which_country
* pt_country: Argentina   <!-- predicted: pt_country: [Argentina]{"entity": "pt_country_code", "value": "AR"}[Argentina]{"entity": "pt_country_code", "value": "AR"} -->
    - slot{"pt_country_code": "AR"}
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_recovered_unhappy_with_dashboard (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_recovered: Número de recuperações em Rossiya.   <!-- predicted: pt_covid_situation_recovered: Número de recuperações em [Rossiya]{"entity": "pt_country_code", "value": "RU"}[Rossiya]{"entity": "pt_country_code", "value": "RU"}. -->
    - slot{"pt_country_code": "RU"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: Polegar para baixo
    - utter_pt_covid_current_statistics


## pt_covid_situation_tested_happy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_tested: Quantos casos de testados há em Mauritania?   <!-- predicted: pt_covid_situation_tested: Quantos casos de testados há em [Mauritania]{"entity": "pt_country_code", "value": "MR"}[Mauritania]{"entity": "pt_country_code", "value": "MR"}? -->
    - slot{"pt_country_code": "MR"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_tested


## pt_covid_situation_tested_unhappy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_tested: Qual é o numero de testados com covid?   <!-- predicted: pt_covid_situation_tested: Qual é o numero de testados com [covid]{"entity": "pt_virus", "value": "COVID"}? -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_tested_unhappy_with_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_tested: "Ilha Esmeralda testados."   <!-- predicted: pt_covid_situation_tested: "[Ilha Esmeralda]{"entity": "pt_country_code", "value": "IE"}[Ilha Esmeralda]{"entity": "pt_country_code", "value": "IE"} testados." -->
    - slot{"pt_country_code": "IE"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: afirmativamente
    - utter_pt_ask_which_country
* pt_country: Qatar   <!-- predicted: pt_country: [Qatar]{"entity": "pt_country_code", "value": "QA"}[Qatar]{"entity": "pt_country_code", "value": "QA"} -->
    - slot{"pt_country_code": "QA"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"new_cases": "987"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_tested


## pt_covid_situation_tested_unhappy_inexistent_country (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_tested: "Ilha Esmeralda testados."   <!-- predicted: pt_covid_situation_tested: "[Ilha Esmeralda]{"entity": "pt_country_code", "value": "IE"}[Ilha Esmeralda]{"entity": "pt_country_code", "value": "IE"} testados." -->
    - slot{"pt_country_code": "IE"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: no ponto
    - utter_pt_ask_which_country
* pt_country: São Tomé e Príncipe   <!-- predicted: pt_country: [São Tomé e Príncipe]{"entity": "pt_country_code", "value": "ST"}[São Tomé e Príncipe]{"entity": "pt_country_code", "value": "ST"} -->
    - slot{"pt_country_code": "ST"}
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_tested_unhappy_with_dashboard (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_tested: Contagem testados em Republic of Liberia   <!-- predicted: pt_covid_situation_tested: Contagem testados em [Republic of Liberia]{"entity": "pt_country_code", "value": "LR"}[Republic of Liberia]{"entity": "pt_country_code", "value": "LR"} -->
    - slot{"pt_country_code": "LR"}
    - action_search_stats   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: negativo
    - utter_pt_covid_current_statistics


## pt_change_bot (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_bot_change_bot: Cosibot Alemão   <!-- predicted: pt_bot_change_bot: [Cosibot Alemão]{"entity": "preferred_lang", "value": "de_lang"}[Cosibot Alemão]{"entity": "preferred_lang", "value": "de_lang"} -->
    - slot{"preferred_lang": "de_lang"}
    - action_change_preferred_language
    - slot{"preferred_lang": "de"}
    - utter_pt_command_change_bot


## pt_covid_situation_infected_municipal_notOk (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Estatísticas de Repabliki ya Afrika-Borwa   <!-- predicted: pt_covid_situation_infected: Estatísticas de [Repabliki ya Afrika-Borwa]{"entity": "pt_country_code", "value": "ZA"}[Repabliki ya Afrika-Borwa]{"entity": "pt_country_code", "value": "ZA"} -->
    - slot{"pt_country_code": "ZA"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_yes: Sim
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation


## pt_covid_situation_infected_municipal_empty (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Contagem infectada ativa em Aljustrel   <!-- predicted: pt_covid_situation_infected: Contagem infectada ativa em [Aljustrel](pt_country_municipal)[Aljustrel](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Aljustrel"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_yes: Afirmativo
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation


## pt_covid_situation_infected_municipal_empty2 (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Atualização em Vila Verde   <!-- predicted: pt_covid_situation_last_update: Atualização em [Vila Verde](pt_country_municipal)[Vila Verde](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Vila Verde"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Abrantes"}
    - slot{"country_municipal_confirmed_accum": 8}
    - utter_country_municipal_hasdata
* pt_covid_situation_last_update: Atualização em Batalha   <!-- predicted: pt_covid_situation_last_update: Atualização em [Batalha](pt_country_municipal)[Batalha](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Batalha"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "empty"}
    - slot{"country_municipal": "Ribeira Brava"}
    - slot{"pt_country_code": "PT"}
    - utter_country_municipal_nodata
* pt_vocative_yes: Sim claro.
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Portugal"}
    - slot{"active_cases": 23775}
    - slot{"new_cases": 0}
    - slot{"total_cases": 28132}
    - slot{"total_recovered": 3182}
    - slot{"total_deaths": 1175}
    - slot{"total_tests": 566172}
    - slot{"new_deaths": 0}
    - slot{"total_infected_critical": 103}
    - utter_pt_covid_situation


## pt_covid_situation_infected_municipal_notOk (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Casos confirmados em Chamusca   <!-- predicted: pt_covid_situation_infected: Casos confirmados em [Chamusca](pt_country_municipal)[Chamusca](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Chamusca"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_no: não senhora
    - utter_pt_further_questions


## pt_covid_situation_infected_municipal_empty (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Contagem infectada ativa em Vila Nova da Barquinha   <!-- predicted: pt_covid_situation_infected: Contagem infectada ativa em [Vila Nova da Barquinha](pt_country_municipal)[Vila Nova da Barquinha](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Vila Nova da Barquinha"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_no: negativa
    - utter_pt_further_questions


## pt_covid_situation_infected_municipa2 (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Última atualização de infetados e mortes em Congo-Quinxassa?   <!-- predicted: pt_covid_situation_last_update: Última atualização de infetados e mortes em [Congo-Quinxassa]{"entity": "pt_country_code", "value": "CD"}[Congo-Quinxassa]{"entity": "pt_country_code", "value": "CD"}? -->
    - slot{"pt_country_code": "CD"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Salvaterra de Magos"}
    - slot{"country_municipal_confirmed_accum": 10}
    - utter_country_municipal_hasdata


## pt_covid_situation_infected_municipa2 (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Atualização em Amarante   <!-- predicted: pt_covid_situation_last_update: Atualização em [Amarante](pt_country_municipal)[Amarante](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Amarante"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Salvaterra de Magos"}
    - slot{"country_municipal_confirmed_accum": 10}
    - utter_country_municipal_hasdata


## pt_covid_situation_infected_region_notOk (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Quantos casos de infetados ativos há em Mann?   <!-- predicted: pt_covid_situation_infected: Quantos casos de infetados ativos há em [Mann]{"entity": "pt_country_code", "value": "IM"}[Mann]{"entity": "pt_country_code", "value": "IM"}? -->
    - slot{"pt_country_code": "IM"}
    - action_search_stats_region   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_region_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_yes: claro
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation


## pt_covid_situation_infected_region_empty (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: casos no total confirmados em Japan   <!-- predicted: pt_covid_situation_infected: casos no total confirmados em [Japan]{"entity": "pt_country_code", "value": "JP"}[Japan]{"entity": "pt_country_code", "value": "JP"} -->
    - slot{"pt_country_code": "JP"}
    - action_search_stats_region   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_region_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_yes: simm
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"new_cases": "517"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation


## pt_covid_situation_infected_region_empty2 (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Atualização em Lamego   <!-- predicted: pt_covid_situation_last_update: Atualização em [Lamego](pt_country_municipal)[Lamego](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Lamego"}
    - action_search_stats_region   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Centro"}
    - slot{"country_region_confirmed_accum": 8}
    - utter_country_region_hasdata   <!-- predicted: utter_country_municipal_hasdata -->
* pt_covid_situation_last_update: Novos casos e mortes em República da Indonésia?   <!-- predicted: pt_covid_situation_last_update: Novos casos e mortes em [República da Indonésia]{"entity": "pt_country_code", "value": "ID"}[República da Indonésia]{"entity": "pt_country_code", "value": "ID"}? -->
    - slot{"pt_country_code": "ID"}
    - action_search_stats_region   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_region_search_successful": "empty"}
    - slot{"country_region": "Algarve"}
    - slot{"pt_country_code": "PT"}
    - utter_country_municipal_nodata
* pt_vocative_yes: sim sim
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Portugal"}
    - slot{"active_cases": 23775}
    - slot{"new_cases": 0}
    - slot{"total_cases": 28132}
    - slot{"total_recovered": 3182}
    - slot{"total_deaths": 1175}
    - slot{"total_tests": 566172}
    - slot{"new_deaths": 0}
    - slot{"total_infected_critical": 103}
    - utter_pt_covid_situation


## pt_covid_situation_infected_region_notOk (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Contagem infectada ativa em Mortágua   <!-- predicted: pt_covid_situation_infected: Contagem infectada ativa em [Mortágua](pt_country_municipal)[Mortágua](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Mortágua"}
    - action_search_stats_region   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_region_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_no: Nem por isso.
    - utter_pt_further_questions


## pt_covid_situation_infected_region_empty (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_infected: Contagem infectados no total em Pombal   <!-- predicted: pt_covid_situation_infected: Contagem infectados no total em [Pombal](pt_country_municipal)[Pombal](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Pombal"}
    - action_search_stats_region   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_region_search_successful": "not-ok"}
    - utter_country_municipal_nodata
* pt_vocative_no: nada
    - utter_pt_further_questions   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_covid_situation_infected_region2 (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation_last_update: Últimos dados de Macedo de Cavaleiros   <!-- predicted: pt_covid_situation_last_update: Últimos dados de [Macedo de Cavaleiros](pt_country_municipal)[Macedo de Cavaleiros](pt_country_municipal) -->
    - slot{"pt_country_municipal": "Macedo de Cavaleiros"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Madeira"}
    - slot{"country_municipal_confirmed_accum": 10}
    - utter_country_region_hasdata   <!-- predicted: utter_country_municipal_hasdata -->


## pt_covid_situation_region_municipal_country_mixed (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_situation: Quantos casos existem em Marinha Grande?   <!-- predicted: pt_covid_situation: Quantos casos existem em [Marinha Grande](pt_country_municipal)[Marinha Grande](pt_country_municipal)? -->
    - slot{"pt_country_municipal": "Marinha Grande"}
    - slot{"pt_country_municipal": "Ribeira Brava"}
    - action_search_stats_municipal   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_municipal_search_successful": "empty"}
    - slot{"country_municipal": "Ribeira Brava"}
    - slot{"pt_country_code": "PT"}
    - utter_country_municipal_nodata
* pt_vocative_yes: Com certeza
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Portugal"}
    - slot{"active_cases": 23937}
    - slot{"new_cases": 0}
    - slot{"total_cases": 28319}
    - slot{"total_recovered": 3198}
    - slot{"total_deaths": 1184}
    - slot{"total_tests": 600061}
    - slot{"new_deaths": 0}
    - slot{"total_infected_critical": 108}
    - utter_pt_covid_situation
* pt_covid_situation: Quantos casos existem em Porto?   <!-- predicted: pt_covid_situation: Quantos casos existem em [Porto](pt_country_municipal)[Porto](pt_country_municipal)? -->
    - slot{"pt_country_municipal": "Porto"}
    - slot{"pt_country_region": "Centro"}
    - action_search_stats_region   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Centro"}
    - slot{"country_region_confirmed_accum": 3569}
    - utter_country_region_hasdata


## pt_prevention_informed (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_prevention_informed: Devo me manter informado?
    - utter_pt_prevention_informed   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_bot_personal_questions (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_bot_personal_questions: Where do you go after work?
    - utter_pt_bot_personal_questions   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_cc_geography (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_cc_geography: A Holanda tem montanhas?   <!-- predicted: pt_cc_geography: A [Holanda]{"entity": "pt_country_code", "value": "NL"}[Holanda]{"entity": "pt_country_code", "value": "NL"} tem montanhas? -->
    - slot{"pt_country_code": "NL"}
    - utter_pt_cc_geography


## pt_covid_sex (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_sex: Relações sexuais e covid   <!-- predicted: pt_covid_sex: Relações sexuais e [covid]{"entity": "pt_virus", "value": "COVID"} -->
    - utter_pt_covid_sex


## carousel-trigger (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* carousel-trigger:    <!-- predicted: None:  -->
    - utter_carousel_trigger   <!-- predicted: action_default_fallback -->


## video-trigger (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* video-trigger:    <!-- predicted: None:  -->
    - utter_video_trigger   <!-- predicted: action_default_fallback -->


## cms-trigger (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* cms-trigger:    <!-- predicted: None:  -->
    - utter_cms_trigger   <!-- predicted: action_default_fallback -->


## start_conversation (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* start: /start_chat   <!-- predicted: start_chat: /start_chat -->
    - action_check_Bot_Introduced   <!-- predicted: utter_pt_want_to_add_country -->
    - slot{"bot_introduced": "True"}
    - utter_pt_welcome


## pt_comment_racist (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_comment_racist: És negro
    - utter_pt_comment_racist   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_coronavirus_info (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_coronavirus_info: information on coronaviruses   <!-- predicted: pt_coronavirus_info: information on [coronaviruses]{"entity": "pt_virus", "value": "COVID"}[coronaviruses]{"entity": "pt_virus", "value": "COVID"} -->
    - utter_pt_coronavirus_info


## pt_covid_aftereffects_immunity (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_aftereffects_immunity: Depois de ter sido infectado fico imune ao vírus?   <!-- predicted: pt_covid_aftereffects_immunity: Depois de ter sido infectado fico imune ao [vírus]{"entity": "pt_virus", "value": "COVID"}[vírus]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_covid_aftereffects_immunity


## pt_covid_babys_children (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_babys_children: As crianças transmitem a doença?   <!-- predicted: pt_covid_babys_children: As crianças transmitem a [doença]{"entity": "pt_virus", "value": "COVID"}[doença]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_covid_babys_children


## pt_covid_cosibot (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_cosibot: Cosibot
    - utter_pt_covid_cosibot   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_covid_current_statistics (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_current_statistics: Informações actualizadas Milwaukee   <!-- predicted: pt_covid_current_statistics: Informações actualizadas [Milwaukee]{"entity": "pt_geography", "value": "town"}[Milwaukee]{"entity": "pt_geography", "value": "town"} -->
    - utter_pt_covid_current_statistics


## pt_covid_incubation (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_incubation: Quanto tempo dura o período de incubação COVID2019?   <!-- predicted: pt_covid_incubation: Quanto tempo dura o período de incubação [COVID2019]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_covid_incubation


## pt_covid_info (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_info: Conta mais sobre o novo coronavírus   <!-- predicted: pt_covid_info: Conta mais sobre o [novo coronavírus]{"entity": "pt_virus", "value": "COVID"}[novo coronavírus]{"entity": "pt_virus", "value": "COVID"} -->
    - utter_pt_covid_info


## pt_covid_meaning (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_meaning: Porque o vírus é chamado assim?   <!-- predicted: pt_covid_meaning: Porque o [vírus]{"entity": "pt_virus", "value": "COVID"}[vírus]{"entity": "pt_virus", "value": "COVID"} é chamado assim? -->
    - utter_pt_covid_meaning


## pt_covid_pregnancy (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_pregnancy: As mulheres grávidas são mais suscetíveis à infeção ou têm maior risco de doenças graves, morbidade ou mortalidade com o COVID-19, em comparação com o   público em geral?   <!-- predicted: pt_covid_pregnancy: As mulheres grávidas são mais suscetíveis à infeção ou têm maior risco de doenças graves, morbidade ou mortalidade com o [COVID-19]{"entity": "pt_virus", "value": "COVID"}, em comparação com o   público em geral? -->
    - utter_pt_covid_pregnancy


## pt_covid_surfaces (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_surfaces: Superfícies de sobrevivência de vírus.   <!-- predicted: pt_covid_surfaces: Superfícies de sobrevivência de [vírus]{"entity": "pt_virus", "value": "COVID"}[vírus]{"entity": "pt_virus", "value": "COVID"}. -->
    - utter_pt_covid_surfaces


## pt_covid_symptoms (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_symptoms: sintomas associados à doença   <!-- predicted: pt_covid_symptoms: sintomas associados à [doença]{"entity": "pt_virus", "value": "COVID"}[doença]{"entity": "pt_virus", "value": "COVID"} -->
    - utter_pt_covid_symptoms


## pt_covid_worry (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_covid_worry: Devo me preocupar com o vírus?   <!-- predicted: pt_covid_worry: Devo me preocupar com o [vírus]{"entity": "pt_virus", "value": "COVID"}[vírus]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_covid_worry


## pt_myth_alcohol (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_myth_alcohol: A pulverização de álcool em todo o corpo mata o vírus.   <!-- predicted: pt_myth_alcohol: A pulverização de álcool em todo o corpo mata o [vírus]{"entity": "pt_virus", "value": "COVID"}[vírus]{"entity": "pt_virus", "value": "COVID"}. -->
    - utter_pt_myth_alcohol


## pt_myth_packages (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_myth_packages: É seguro receber uma carta de qualquer área em que o COVID-19 tenha sido relatado?   <!-- predicted: pt_myth_packages: É seguro receber uma carta de qualquer área em que o [COVID-19]{"entity": "pt_virus", "value": "COVID"}[COVID-19]{"entity": "pt_virus", "value": "COVID"} tenha sido relatado? -->
    - utter_pt_myth_packages


## pt_myth_transmission_hot_areas (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_myth_transmission_hot_areas: O clima quente vai parar o surto de COVID-19?   <!-- predicted: pt_myth_transmission_hot_areas: O clima quente vai parar o surto de [COVID-19]{"entity": "pt_virus", "value": "COVID"}[COVID-19]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_myth_transmission_hot_areas


## pt_portugal_ill_no_covid (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_portugal_ill_no_covid: Quem devem contactar os utentes sem suspeita de COVID-19?   <!-- predicted: pt_portugal_ill_no_covid: Quem devem contactar os utentes sem suspeita de [COVID-19]{"entity": "pt_virus", "value": "COVID"}[COVID-19]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_portugal_ill_no_covid


## pt_portugal_rates (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_portugal_rates: Qual é a percentagem de casos de doença?   <!-- predicted: pt_portugal_rates: Qual é a percentagem de casos de [doença]{"entity": "pt_virus", "value": "COVID"}[doença]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_portugal_rates


## pt_prevention_medicine (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_prevention_medicine: Tratamento covid-19   <!-- predicted: pt_prevention_medicine: Tratamento [covid-19]{"entity": "pt_virus", "value": "COVID"} -->
    - utter_pt_prevention_medicine


## pt_sources (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_sources: sns24
    - utter_pt_sources   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_spread_animals (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_spread_animals: Os seres humanos podem ser infectados com o COVID-19 a partir de fontes   <!-- predicted: pt_spread_animals: Os seres humanos podem ser infectados com o [COVID-19]{"entity": "pt_virus", "value": "COVID"}[COVID-19]{"entity": "pt_virus", "value": "COVID"} a partir de fontes -->
    - utter_pt_spread_animals


## pt_spread_feces (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_spread_feces: Posso pegar o COVID-19?   <!-- predicted: pt_covid_worry: Posso pegar o [COVID-19]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_spread_feces   <!-- predicted: utter_pt_covid_worry -->


## pt_spread_general (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_spread_general: cómo se propagó el virus   <!-- predicted: pt_spread_general: cómo se propagó el [virus]{"entity": "pt_virus", "value": "COVID"}[virus]{"entity": "pt_virus", "value": "COVID"} -->
    - utter_pt_spread_general   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_spread_pets (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_spread_pets: O meu animal de estimação da família pode espalhar o virus?   <!-- predicted: pt_spread_pets: O meu animal de estimação da família pode espalhar o [virus]{"entity": "pt_virus", "value": "COVID"}[virus]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_spread_pets


## pt_spread_risk (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_spread_risk: Quais são as chances de poder ser infetado pelo COVID-19?   <!-- predicted: pt_spread_risk: Quais são as chances de poder ser infetado pelo [COVID-19]{"entity": "pt_virus", "value": "COVID"}[COVID-19]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_spread_risk


## pt_spread_surfaces_food_objects (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_spread_surfaces_food_objects: o coronavírus pode ser transmitido através dos alimentos?   <!-- predicted: pt_spread_surfaces_food_objects: o [coronavírus]{"entity": "pt_virus", "value": "COVID"} pode ser transmitido através dos alimentos? -->
    - utter_pt_spread_surfaces_food_objects   <!-- predicted: action_default_fallback -->


## pt_test_general (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_test_general: Devo ser testado para o COVID-19?   <!-- predicted: pt_test_general: Devo ser testado para o [COVID-19]{"entity": "pt_virus", "value": "COVID"}[COVID-19]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_test_general


## pt_test_per_day (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_test_per_day: quantos testes ao covid foram realizados diariamente em portugal nos ultimos 5   <!-- predicted: pt_test_per_day: quantos testes ao [covid]{"entity": "pt_virus", "value": "COVID"}[covid]{"entity": "pt_virus", "value": "COVID"} foram realizados diariamente em portugal nos ultimos 5 -->
    - utter_pt_test_per_day


## pt_travel_after (/tmp/tmp3h1cbgt7/6c7aa61c4d314ca49619194a3bc278ec_conversation_tests.md)
* pt_travel_after: O que fazer depois de viajar.
    - utter_pt_travel_after   <!-- predicted: action_default_fallback -->


