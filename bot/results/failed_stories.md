## pt_economy_consequences (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_economy_consequences: Economia e [coronavirus]{"entity": "pt_virus", "value": "COVID"}
    - utter_pt_economy_consequences   <!-- predicted: action_default_fallback -->


## pt_features_date (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_features_date: Consegues dizer-me que dia é hoje?
    - utter_pt_features_date   <!-- predicted: action_get_date -->


## pt_features_time (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_features_time: Podes dizer-me as horas que são?
    - utter_pt_features_time   <!-- predicted: action_get_time -->


## pt_mask_use_after (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_mask_use_after: Como retirar a máscara?
    - utter_pt_mask_use_after   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_portugal_rates (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_portugal_rates: Qual é a percentagem de casos de doença ligeira e grave por [COVID-19]{"entity": "pt_virus", "value": "COVID"}?   <!-- predicted: pt_portugal_rates: Qual é a percentagem de casos de [doença]{"entity": "pt_virus", "value": "COVID"} ligeira e grave por [COVID-19]{"entity": "pt_virus", "value": "COVID"}? -->
    - utter_pt_portugal_rates   <!-- predicted: action_default_fallback -->


## pt_prevention_medicine (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_prevention_medicine: Sobre vacinas para [COVID-19]{"entity": "pt_virus", "value": "COVID"}.
    - utter_pt_prevention_medicine   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_spread_phases (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_spread_phases: Em que fase do surto está [Portugal]{"entity": "pt_country_code", "value": "PT"}?   <!-- predicted: pt_spread_phases: Em que fase do surto está Portugal? -->
    - utter_pt_spread_phases


## pt_state_emergency_end (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_state_emergency_end: Situação de emergência em [Portugal]{"entity": "pt_country_code", "value": "PT"}, até quando?   <!-- predicted: pt_covid_situation: Situação de emergência em Portugal, até quando? -->
    - utter_pt_state_emergency_end   <!-- predicted: action_default_fallback -->


## pt_bot_personality (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_bot_personality: És muito simpático?   <!-- predicted: pt_comment_positive: És muito simpático? -->
    - utter_pt_bot_personality   <!-- predicted: utter_pt_comment_positive -->


## pt_test_per_day (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_test_per_day: Testes por dia?
    - utter_pt_test_per_day   <!-- predicted: utter_pt_bot_languages -->
    - action_listen   <!-- predicted: utter_pt_bot_languages -->


## pt_cc_geography (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_cc_geography: O que sabes sobre a [Inglaterra]{"entity": "pt_country_code", "value": "GB"}?
    - utter_pt_cc_geography   <!-- predicted: action_default_fallback -->


## pt_covid_info (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_info: O que é o [Covid19]{"entity": "pt_virus", "value": "COVID"}?
    - utter_pt_covid_info   <!-- predicted: action_default_fallback -->


## pt_covid_sex (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_sex: Sexo e [coronavirus]{"entity": "pt_virus", "value": "COVID"}   <!-- predicted: pt_covid_sex: Sexo e coronavirus -->
    - utter_pt_covid_sex


## pt_covid_situation_unhappy (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation: quantas pessoas morreram hoje?
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_unhappy_inexistent_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation: Notícias [Turquemenistao]{"entity": "pt_country_code", "value": "TM"}   <!-- predicted: pt_covid_situation: Notícias [Turquemenistao](pt_country_code) -->
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Turquemenistao]{"entity": "pt_country_code", "value": "TM"}   <!-- predicted: pt_country: [Turquemenistao](pt_country_code) -->
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_unhappy_with_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation: Quais são os paises com mais casos?   <!-- predicted: pt_state_emergency_run: Quais são os paises com mais casos? -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Portugal]{"entity": "pt_country_code", "value": "PT"}
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


## pt_covid_situation_deaths_happy (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_deaths: quantas mortes em [Suécia]{"entity": "pt_country_code", "value": "SE"}   <!-- predicted: pt_covid_situation: quantas mortes em [Suécia]{"entity": "pt_country_code", "value": "SE"} -->
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
    - utter_pt_covid_situation_deaths   <!-- predicted: utter_pt_covid_situation -->


## pt_covid_situation_deaths_unhappy (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_deaths: numero de mortes em [Turquemenistao]{"entity": "pt_country_code", "value": "TM"}   <!-- predicted: pt_covid_situation: numero de mortes em [Turquemenistao](pt_country_code) -->
    - action_search_stats
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_deaths_unhappy_with_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_deaths: qual o numero de mortos em [Itália]{"entity": "pt_country_code", "value": "IT"}   <!-- predicted: pt_covid_situation: qual o numero de mortos em [Itália]{"entity": "pt_country_code", "value": "IT"} -->
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Itália]{"entity": "pt_country_code", "value": "IT"}
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
    - utter_pt_covid_situation_deaths   <!-- predicted: utter_pt_covid_situation -->


## pt_covid_situation_deaths_unhappy_inexistent_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_deaths: contagem de mortes em [Turquemenistao]{"entity": "pt_country_code", "value": "TM"}   <!-- predicted: pt_covid_situation: contagem de mortes em [Turquemenistao](pt_country_code) -->
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Turquemenistao]{"entity": "pt_country_code", "value": "TM"}   <!-- predicted: pt_country: [Turquemenistao](pt_country_code) -->
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_infected_unhappy (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_infected: contagem de infetados em [Itália]{"entity": "pt_country_code", "value": "IT"}   <!-- predicted: pt_covid_situation: contagem de infetados em [Itália]{"entity": "pt_country_code", "value": "IT"} -->
    - action_search_stats
    - slot{"search_successful": "not-ok"}
    - utter_pt_covid_current_statistics


## pt_covid_situation_infected_unhappy_inexistent_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_infected: qual o número de casos por [Covid-19]{"entity": "pt_virus", "value": "COVID"} em [Turquemenistao]{"entity": "pt_country_code", "value": "TM"}   <!-- predicted: pt_covid_situation_infected: qual o número de casos por [Covid-19]{"entity": "pt_virus", "value": "COVID"} em [Turquemenistao](pt_country_code) -->
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Turquemenistao]{"entity": "pt_country_code", "value": "TM"}   <!-- predicted: pt_country: [Turquemenistao](pt_country_code) -->
    - action_search_stats
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics


## pt_covid_situation_infected_unhappy_with_dashboard (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_infected: contagem de infetados em [Itália]{"entity": "pt_country_code", "value": "IT"}   <!-- predicted: pt_covid_situation: contagem de infetados em [Itália]{"entity": "pt_country_code", "value": "IT"} -->
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_no: não
    - utter_pt_covid_current_statistics


## pt_covid_situation_infected_critical_unhappy_inexistent_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_infected_critical: Contagem infectados alarmantes no [Taiwan Area]{"entity": "pt_country_code", "value": "TW"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Taiwan Area]{"entity": "pt_country_code", "value": "TW"}
    - slot{"search_successful": "inexistent-country"}
    - utter_pt_covid_no_country_current_statistics   <!-- predicted: action_search_stats -->


## pt_covid_situation_last_update_unhappy_with_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_last_update: Fala sobre atualização de casos
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Mexico]{"entity": "pt_country_code", "value": "MX"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Mexico"}
    - slot{"new_cases": "987"}
    - slot{"total_cases": "17543"}
    - slot{"total_recovered": "921"}
    - slot{"total_deaths": "756"}
    - slot{"total_tests": "233300"}
    - slot{"total_infected_critical": "176"}
    - utter_pt_covid_situation_last_update


## pt_bot_hobbies (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_bot_hobbies: O que fazes para te divertires?
    - utter_pt_bot_hobbies   <!-- predicted: action_default_fallback -->


## pt_covid_situation_tested_unhappy_with_country (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_covid_situation_tested: Quantos testes foram realizados até à data?
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "wrong-country"}
    - utter_pt_want_to_add_country
* pt_vocative_yes: sim
    - utter_pt_ask_which_country
* pt_country: [Hong Kong]{"entity": "pt_country_code", "value": "HK"}
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


## pt_bot_languages (/tmp/tmp2wdks9lu/b1aa7b0cdda6454d984c6dd18de34bc1_conversation_tests.md)
* pt_bot_languages: Falas em inglês?   <!-- predicted: pt_bot_languages: Falas em [inglês](language)? -->
    - utter_pt_bot_languages


