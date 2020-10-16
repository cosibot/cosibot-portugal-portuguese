## start_conversation
* start: /start_chat
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_pt_welcome


<!--## start
* start: /start_chat
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_pt_welcome

## start
* start: /start-dialogue
  - utter_pt_greeting_hello

## start1_1
* start-dialogue: 
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_pt_welcome

## start1_2
* start-dialogue: 
  - utter_pt_greeting_hello

## pt_greeting_hello
* pt_greeting_hello: Aloha
  - utter_pt_greeting_hello

## pt_greeting_hello_1
* pt_greeting_hello: ei tu
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_pt_welcome
-->
## pt_bot_appearance
* pt_bot_appearance: Explica-me como é que te aparentas
  - utter_pt_bot_appearance

## pt_bot_availability
* pt_bot_availability: Estás disponível todo o dia?
  - utter_pt_bot_availability

## pt_bot_books
* pt_bot_books: Livro preferido
  - utter_pt_bot_books

## pt_bot_capabilities
* pt_bot_capabilities: Precisas de alguém com quem falar?
  - utter_pt_bot_capabilities

## pt_bot_fear
* pt_bot_fear: Qual o teu medo?
  - utter_pt_bot_fear

## pt_bot_goal
* pt_bot_goal: Qual a tua ambição?
  - utter_pt_bot_goal

## pt_bot_languages
* pt_bot_languages: Outra língua.
  - utter_pt_bot_languages

## pt_bot_movies
* pt_bot_movies: Quais são os teus filmes preferidos
  - utter_pt_bot_movies

## pt_bot_music
* pt_bot_music: Grupo musical preferido
  - utter_pt_bot_music

## pt_bot_name
* pt_bot_name: Para quem estou a falar?
  - utter_pt_bot_name

## pt_bot_origin
* pt_bot_origin: De onde é que vens?
  - utter_pt_bot_origin

## pt_bot_personality
* pt_bot_personality: O que achas da tua personalidade?
  - utter_pt_bot_personality

## pt_bot_real
* pt_bot_real: és uma pessoa ou robô?
  - utter_pt_bot_real

## pt_bot_residence
* pt_bot_residence: Diz-me onde te encontras.
  - utter_pt_bot_residence

## pt_bot_sexual
* pt_bot_sexual: Já alguma vez tiveste um orgasmo?
  - utter_pt_bot_sexual

## pt_bot_version
* pt_bot_version: Em que versão estás?
  - utter_pt_bot_version

## pt_cc_chicken_egg
* pt_cc_chicken_egg: Galinha ou ovo primeiro?
  - utter_pt_cc_chicken_egg

## pt_cc_joke
* pt_cc_joke: Consegues contar-me algo engraçado?
  - utter_pt_cc_joke

## pt_cc_lets_talk
* pt_cc_lets_talk: Podes conversar?
  - utter_pt_cc_lets_talk

## pt_cc_moon
* pt_cc_moon: distância da lua
  - utter_pt_cc_moon

## pt_cc_newspaper
* pt_cc_newspaper: Quais são as novidades?
  - utter_pt_cc_newspaper

## pt_cc_philosophical
* pt_cc_philosophical: Como é que os humanos enquanto espécie se extinguirão?
  - utter_pt_cc_philosophical

## pt_cc_politics
* pt_cc_politics: Qual tipo de sistema politico governa no teu país?
  - utter_pt_cc_politics

## pt_cc_religion
* pt_cc_religion: Onde é que Deus nos mostra piedade?
  - utter_pt_cc_religion

## pt_cc_weather
* pt_cc_weather: O sol tem estado a brilhar?
  - utter_pt_cc_weather

## pt_comment_negative
* pt_comment_negative: Essa resposta está errada.
  - utter_pt_comment_negative

## pt_comment_offense
* pt_comment_offense: Vai e sai-me da frente
  - utter_pt_comment_offense

## pt_comment_positive
* pt_comment_positive: Tu és simpático
  - utter_pt_comment_positive

## pt_comment_racist
* pt_comment_racist: És negro
  - utter_pt_comment_racist

## pt_comment_smart
* pt_comment_smart: És tão astuto
  - utter_pt_comment_smart

## pt_coronavirus_info
* pt_coronavirus_info: information on coronaviruses
  - utter_pt_coronavirus_info

## pt_covid_aftereffects_immunity
* pt_covid_aftereffects_immunity: Depois de ter sido infectado fico imune ao vírus?
  - utter_pt_covid_aftereffects_immunity

## pt_covid_alike
* pt_covid_alike: Surtos semelhantes a esta pandemia
  - utter_pt_covid_alike

## pt_covid_babys_children
* pt_covid_babys_children: As crianças transmitem a doença?
  - utter_pt_covid_babys_children

## pt_covid_close_contact
* pt_covid_close_contact: Contactos próximos
  - utter_pt_covid_close_contact

## pt_covid_community_transmission
* pt_covid_community_transmission: Área de transmissão comunitária.
  - utter_pt_covid_community_transmission

## pt_covid_cosibot
* pt_covid_cosibot: Cosibot
  - utter_pt_covid_cosibot

## pt_covid_crisis_howlong
* pt_covid_crisis_howlong: Quando é que esta crise vai a acabar?
  - utter_pt_covid_crisis_howlong

## pt_covid_current_statistics
* pt_covid_current_statistics: Informações actualizadas Milwaukee
  - utter_pt_covid_current_statistics

## pt_covid_duration
* pt_covid_duration: Por quanto tempo posso ficar doente?
  - utter_pt_covid_duration

## pt_covid_incubation
* pt_covid_incubation: Quanto tempo dura o período de incubação COVID2019?
  - utter_pt_covid_incubation

## pt_covid_info
* pt_covid_info: Conta mais sobre o novo coronavírus
  - utter_pt_covid_info

## pt_covid_meaning
* pt_covid_meaning: Porque o vírus é chamado assim?
  - utter_pt_covid_meaning

## pt_covid_mortality_rate
* pt_covid_mortality_rate: qual a percentagem de letalidade ?
  - utter_pt_covid_mortality_rate

## pt_covid_pandemic
* pt_covid_pandemic: Pandemia
  - utter_pt_covid_pandemic

## pt_covid_pregnancy
* pt_covid_pregnancy: As mulheres grávidas são mais suscetíveis à infeção ou têm maior risco de doenças graves, morbidade ou mortalidade com o COVID-19, em comparação com o   público em geral?
	- utter_pt_covid_pregnancy

## pt_covid_preexisting_illness
* pt_covid_preexisting_illness: Diabetes
  - utter_pt_covid_preexisting_illness

## pt_covid_sars
* pt_covid_sars: Diferenças entre COVID19 e SARS
  - utter_pt_covid_sars

## pt_covid_surfaces
* pt_covid_surfaces: Superfícies de sobrevivência de vírus.
  - utter_pt_covid_surfaces

## pt_covid_symptoms
* pt_covid_symptoms: sintomas associados à doença
  - utter_pt_covid_symptoms

## pt_covid_worry
* pt_covid_worry: Devo me preocupar com o vírus?
  - utter_pt_covid_worry

## pt_features_date
* pt_features_date: Não sei a data.
  - action_get_date

## pt_features_time
* pt_features_time: Diz que horas são.
  - action_get_time

## pt_greeting_goodbye
* pt_greeting_goodbye: Saindo...
  - utter_pt_greeting_goodbye

## pt_greeting_how_are_you
* pt_greeting_how_are_you: Como te sentes
  - utter_pt_greeting_how_are_you

## pt_mask_general
* pt_mask_general: Devo usar uma máscara?
  - utter_pt_mask_general

## pt_mask_use_after
* pt_mask_use_after: descartar
  - utter_pt_mask_use_after

## pt_mask_use_put
* pt_mask_use_put: Como proceder antes de colocar uma máscara médica?
  - utter_pt_mask_use_put

## pt_myth_alcohol
* pt_myth_alcohol: A pulverização de álcool em todo o corpo mata o vírus.
  - utter_pt_myth_alcohol

## pt_myth_packages
* pt_myth_packages: É seguro receber uma carta de qualquer área em que o COVID-19 tenha sido relatado?
  - utter_pt_myth_packages

## pt_myth_transmission_hot_areas
* pt_myth_transmission_hot_areas: O clima quente vai parar o surto de COVID-19?
  - utter_pt_myth_transmission_hot_areas

## pt_patient_home
* pt_patient_home: É necessário o internamento em todos os casos?
  - utter_pt_patient_home

## pt_patient_referral
* pt_patient_referral: Para onde vão os doentes?
  - utter_pt_patient_referral

## pt_portugal_government_measures
* pt_portugal_government_measures: Medidas do governo
  - utter_pt_portugal_government_measures

## pt_portugal_ill_foreigner
* pt_portugal_ill_foreigner: Estou doente e sou estrangeiro.
  - utter_pt_portugal_ill_foreigner

## pt_portugal_ill_no_covid
* pt_portugal_ill_no_covid: Quem devem contactar os utentes sem suspeita de COVID-19?
  - utter_pt_portugal_ill_no_covid

## pt_portugal_rates
* pt_portugal_rates: Qual é a percentagem de casos de doença?
  - utter_pt_portugal_rates

## pt_prevention_clean_hands
* pt_prevention_clean_hands: Importância de lavar as mãos.
  - utter_pt_prevention_clean_hands

## pt_prevention_distance
* pt_prevention_distance: A que distância devo estar de alguém a tossir ou espirrar?
  - utter_pt_prevention_distance

## pt_prevention_entering_home
* pt_prevention_entering_home: Entrar em casa
  - utter_pt_prevention_entering_home

## pt_prevention_food
* pt_prevention_food: Que cuidados devo ter na preparação e confeção de alimentos?
  - utter_pt_prevention_food

## pt_prevention_general
* pt_prevention_general: como ajudar
  - utter_pt_prevention_general

## pt_prevention_gloves
* pt_prevention_gloves: Quando é que devo usar luvas?
  - utter_pt_prevention_gloves

## pt_prevention_home
* pt_prevention_home: Será melhor ficar em casa se me sentir mal?
  - utter_pt_prevention_home

## pt_prevention_measures
* pt_prevention_measures: Medidas não eficazes.
  - utter_pt_prevention_measures

## pt_prevention_medicine
* pt_prevention_medicine: Tratamento covid-19
  - utter_pt_prevention_medicine

## pt_prevention_respiratory_hygiene
* pt_prevention_respiratory_hygiene: Boa higiene respiratória.
  - utter_pt_prevention_respiratory_hygiene

## pt_prevention_touch
* pt_prevention_touch: Posso tocar nos olhos?
  - utter_pt_prevention_touch

## pt_quarantine_children
* pt_quarantine_children: há subsídios para apoio às famílias?
  - utter_pt_quarantine_children

## pt_quarantine_dos_and_donts
* pt_quarantine_dos_and_donts: posso sair à rua?
  - utter_pt_quarantine_dos_and_donts

## pt_quarantine_toiletpaper
* pt_quarantine_toiletpaper: Porque é as pessoas andam a comprar tanto papel higiénico?
  - utter_pt_quarantine_toiletpaper

## pt_sources
* pt_sources: sns24
  - utter_pt_sources

## pt_spread_air
* pt_spread_air: Pode ser espalhado pelo ar?
  - utter_pt_spread_air

## pt_spread_animals
* pt_spread_animals: Os seres humanos podem ser infectados com o COVID-19 a partir de fontes
  - utter_pt_spread_animals

## pt_spread_feces
* pt_spread_feces: Posso pegar o COVID-19?
  - utter_pt_spread_feces

## pt_spread_general
* pt_spread_general: cómo se propagó el virus
  - utter_pt_spread_general

## pt_spread_no_symptoms
* pt_spread_no_symptoms: Posso adquirir COVID-19 de pessoas sem sintomas?
  - utter_pt_spread_no_symptoms

## pt_spread_pets
* pt_spread_pets: O meu animal de estimação da família pode espalhar o virus?
  - utter_pt_spread_pets

## pt_spread_risk
* pt_spread_risk: Quais são as chances de poder ser infetado pelo COVID-19?
  - utter_pt_spread_risk

## pt_spread_surfaces_food_objects
* pt_spread_surfaces_food_objects: o coronavírus pode ser transmitido através dos alimentos?
  - utter_pt_spread_surfaces_food_objects

## pt_state_emergency_info
* pt_state_emergency_info: o que é estado de emergência?
  - utter_pt_state_emergency_info

## pt_state_emergency_run
* pt_state_emergency_run: Posso correr na rua?
  - utter_pt_state_emergency_run

## pt_test_general
* pt_test_general: Devo ser testado para o COVID-19?
  - utter_pt_test_general

## pt_test_per_day
* pt_test_per_day: quantos testes ao covid foram realizados diariamente em portugal nos ultimos 5
  - utter_pt_test_per_day

## pt_test_what
* pt_test_what: Como é feito o teste?
  - utter_pt_test_what

## pt_test_where
* pt_test_where: Onde posso fazer o despiste?
  - utter_pt_test_where

## pt_travel_after
* pt_travel_after: O que fazer depois de viajar.
  - utter_pt_travel_after

## pt_travel_before
* pt_travel_before: Precaução de viagem.
  - utter_pt_travel_before

## pt_travel_while
* pt_travel_while: Como faço durante a viagem
  - utter_pt_travel_while

## pt_user_angry
* pt_user_angry: Estou tão furioso!
  - utter_pt_user_angry

## pt_user_friend
* pt_user_friend: queres ser o meu amigo?
  - utter_pt_user_friend

## pt_user_happy
* pt_user_happy: Estou extasiado
  - utter_pt_user_happy

## pt_user_love
* pt_user_love: Dás-me a honra de casar contigo?
  - utter_pt_user_love

## pt_user_no_further_questions
* pt_user_no_further_questions: Elucidaste todas as minhas questões, obrigada.
  - utter_pt_user_no_further_questions

## pt_user_particles
* pt_user_particles: Hmm
  - utter_pt_user_particles

## pt_user_scared
* pt_user_scared: Estou super assustada!
  - utter_pt_user_scared

## pt_vocative_call
* pt_vocative_call: Por favor continua
  - utter_pt_vocative_call

## pt_vocative_help
* pt_vocative_help: Podes dar-me assistência?
  - utter_pt_vocative_help

## pt_vocative_sorry
* pt_vocative_sorry: Desculpa
  - utter_pt_vocative_sorry

## pt_vocative_thank_you
* pt_vocative_thank_you: tudo o que posso dizer é obrigado
  - utter_pt_vocative_thank_you

## pt_vocative_you_welcome
* pt_vocative_you_welcome: Era o mínimo que podia fazer.
  - utter_pt_vocative_you_welcome

<!-- 
GENERAL SITUATION 
-->

## pt_covid_situation_without_country
* pt_covid_situation: Como está a situação em Ucrânia?
  - utter_pt_want_to_add_country
* pt_vocative_yes: sem dúvida
  - utter_pt_ask_which_country
* pt_country: Guyane
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

## covid_situation_without_country2
* pt_covid_situation: Quantos mortos houve em portugal hoje?
  - utter_pt_want_to_add_country
* pt_vocative_no: certamente que não
  - utter_pt_further_questions


## covid_situation_without_country3
* pt_covid_situation: Estatísticas actualizadas em Singapura
  - utter_pt_want_to_add_country
* pt_country: Guyane
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

<!-- ### -->

## pt_covid_situation_happy
* pt_covid_situation: Quantos infectados existem neste momento em Região de Lisboa
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
  - utter_pt_covid_situation

## pt_covid_situation_unhappy
* pt_covid_situation: quantos mortos em portugal?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_pt_covid_current_statistics

## pt_covid_situation_unhappy_with_country
* pt_covid_situation: numeros para Região Norte hoje
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: Uhum.
  - utter_pt_ask_which_country
* pt_country: Andorra
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

## pt_covid_situation_unhappy_inexistent_country
* pt_covid_situation: Quantos casos existem em Murça?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: totalmente
  - utter_pt_ask_which_country
* pt_country: Costa Rica
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_pt_covid_no_country_current_statistics

## pt_covid_situation_unhappy_with_dashboard
* pt_covid_situation: Quantos casos existem em Évora?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_no: nunca, de todo
  - utter_pt_covid_current_statistics

<!-- 
DEATHS
-->

## pt_covid_situation_deaths_happy
* pt_covid_situation_deaths: Mortes em República do Uzbequistão
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

## pt_covid_situation_deaths_unhappy
* pt_covid_situation_deaths: Qual é o número de mortos em República de Guinea Ecuatorial?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_pt_covid_current_statistics

## pt_covid_situation_deaths_unhappy_general_with_country
* pt_covid_situation_deaths: Número total de mortos em Malawi?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: yep
  - utter_pt_ask_which_country
* pt_country: Bulgária
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

## pt_covid_situation_deaths_unhappy_with_country
* pt_covid_situation_deaths: Qual é o número de mortos em República de Guinea Ecuatorial?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: está certo
  - utter_pt_ask_which_country
* pt_country: Tanzania
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

## pt_covid_situation_deaths_unhappy_inexistent_country
* pt_covid_situation_deaths: República Federal da Alemã mortes.
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: sim sim
  - utter_pt_ask_which_country
* pt_country: Myanmar
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_pt_covid_no_country_current_statistics

## pt_covid_situation_deaths_unhappy_with_dashboard
* pt_covid_situation_deaths: Quantos mortos existem neste momento em HIMI?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_no: de jeito nenhum
  - utter_pt_covid_current_statistics

<!-- 
INFECTED
-->

## pt_covid_situation_infected_happy
* pt_covid_situation_infected: Contagem infectados no total em Calheta (São Jorge){"entity": "pt_country_municipal", "value": "Calheta (São Jorge)"}
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

## pt_covid_situation_infected_unhappy
* pt_covid_situation_infected: quantos casos há em Reino da Jordânia no momento?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_pt_covid_current_statistics

## pt_covid_situation_infected_unhappy_with_country
* pt_covid_situation_infected: Casos confirmados em Região Autónoma dos Açores
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: Sim, por favor
  - utter_pt_ask_which_country
* pt_country: Canadá
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

## pt_covid_situation_infected_unhappy_inexistent_country
* pt_covid_situation_infected: Número de infectados ativos em Northern Ireland.
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: yep
  - utter_pt_ask_which_country
* pt_country: São Marino
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_pt_covid_no_country_current_statistics

## pt_covid_situation_infected_unhappy_with_dashboard
* pt_covid_situation_infected: Qual é o número de casos confirmados em Seixal
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_no: Provavelmente não.
  - utter_pt_covid_current_statistics

<!-- 
INFECTED CRITICAL
-->

## pt_covid_situation_infected_critical_happy
* pt_covid_situation_infected_critical: Contagem infectada crítica em Bonaire, Sint Eustatius and Saba
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

## pt_covid_situation_infected_critical_unhappy
* pt_covid_situation_infected_critical: Contagem infectados graves no South Korea
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_pt_covid_current_statistics

## pt_covid_situation_infected_critical_unhappy_with_country
* pt_covid_situation_infected_critical: Contagem infectados alarmantes em República dos Camarões
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: naturalmente
  - utter_pt_ask_which_country
* pt_country: Burquina
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

## pt_covid_situation_infected_critical_unhappy_inexistent_country
* pt_covid_situation_infected_critical: Número de infectados graves em Luxemburgo.
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: Certo.
  - utter_pt_ask_which_country
* pt_country: no Zimbabué
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_pt_covid_no_country_current_statistics

## pt_covid_situation_infected_critical_unhappy_with_dashboard
* pt_covid_situation_infected_critical: Número de casos criticos em São Vicente e Granadinas
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_no: Claro que não.
  - utter_pt_covid_current_statistics

<!-- 
LAST UPDATE 
-->

## pt_covid_situation_last_update_happy
* pt_covid_situation_last_update: Atualização em Montalegre
  - action_search_stats
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

## pt_covid_situation_last_update_unhappy
* pt_covid_situation_last_update: Atualização em Trofa
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_pt_covid_current_statistics

## pt_covid_situation_last_update_unhappy_with_country
* pt_covid_situation_last_update: Ultima atualização em República de San Marino
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: mesmo na muche
  - utter_pt_ask_which_country
* pt_country: Croacia
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

## pt_covid_situation_last_update_unhappy_inexistent_country
* pt_covid_situation_last_update: Atualização em Seia
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: Sim
  - utter_pt_ask_which_country
* pt_country: Samoa
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_pt_covid_no_country_current_statistics

## pt_covid_situation_last_update_unhappy_with_dashboard
* pt_covid_situation_last_update: Atualização em Castelo de Paiva
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_no: negativa
  - utter_pt_covid_current_statistics

<!-- 
SITUATION RECOVERED
-->

## pt_covid_situation_recovered_happy
* pt_covid_situation_recovered: Quantos casos de recuperados há em República da Coreia?
  - action_search_stats
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

## pt_covid_situation_recovered_unhappy
* pt_covid_situation_recovered: qual o numero de recuperados em Federation of Saint Christopher and Nevis?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_pt_covid_current_statistics

## pt_covid_situation_recovered_unhappy_with_country
* pt_covid_situation_recovered: Numero de recuperações em São Marino hoje?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: mesmo na muche
  - utter_pt_ask_which_country
* pt_country: Aruba
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

## pt_covid_situation_recovered_unhappy_inexistent_country
* pt_covid_situation_recovered: Quantos recuperados tem Chad?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: yep
  - utter_pt_ask_which_country
* pt_country: Argentina
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_pt_covid_no_country_current_statistics

## pt_covid_situation_recovered_unhappy_with_dashboard
* pt_covid_situation_recovered: Número de recuperações em Rossiya.
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_no: Polegar para baixo
  - utter_pt_covid_current_statistics

<!-- 
TESTED
-->

## pt_covid_situation_tested_happy
* pt_covid_situation_tested: Quantos casos de testados há em Mauritania?
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
  - utter_pt_covid_situation_tested

## pt_covid_situation_tested_unhappy
* pt_covid_situation_tested: Qual é o numero de testados com covid?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_pt_covid_current_statistics

## pt_covid_situation_tested_unhappy_with_country
* pt_covid_situation_tested: "Ilha Esmeralda testados."
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: afirmativamente
  - utter_pt_ask_which_country
* pt_country: Qatar
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

## pt_covid_situation_tested_unhappy_inexistent_country
* pt_covid_situation_tested: "Ilha Esmeralda testados."
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_yes: no ponto
  - utter_pt_ask_which_country
* pt_country: São Tomé e Príncipe
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_pt_covid_no_country_current_statistics

## pt_covid_situation_tested_unhappy_with_dashboard
* pt_covid_situation_tested: Contagem testados em Republic of Liberia
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_pt_want_to_add_country
* pt_vocative_no: negativo
  - utter_pt_covid_current_statistics

## pt_change_bot
* pt_bot_change_bot: Cosibot Alemão
  - action_change_preferred_language
  - slot{"preferred_lang": "de"}
  - utter_pt_command_change_bot

## pt_news_request
* pt_news_request: Quais são as últimas noticias?
  - action_get_news_request

## pt_covid_situation_infected_municipal_notOk
* pt_covid_situation_infected: Estatísticas de Repabliki ya Afrika-Borwa
  - action_search_stats_municipal
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

## pt_covid_situation_infected_municipal_empty
* pt_covid_situation_infected: Contagem infectada ativa em Aljustrel
  - action_search_stats_municipal
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

## pt_covid_situation_infected_municipal_empty2
* pt_covid_situation_last_update: Atualização em Vila Verde
    - action_search_stats_municipal
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Abrantes"}
    - slot{"country_municipal_confirmed_accum": 8}
    - utter_country_municipal_hasdata
* pt_covid_situation_last_update: Atualização em Batalha
    - action_search_stats_municipal
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

## pt_covid_situation_infected_municipal_notOk
* pt_covid_situation_infected: Casos confirmados em Chamusca
  - action_search_stats_municipal
  - slot{"country_municipal_search_successful": "not-ok"}
  - utter_country_municipal_nodata
* pt_vocative_no: não senhora
  - utter_pt_further_questions

## pt_covid_situation_infected_municipal_empty
* pt_covid_situation_infected: Contagem infectada ativa em Vila Nova da Barquinha
  - action_search_stats_municipal
  - slot{"country_municipal_search_successful": "not-ok"}
  - utter_country_municipal_nodata
* pt_vocative_no: negativa
  - utter_pt_further_questions


## pt_covid_situation_infected_municipa2
* pt_covid_situation_last_update: Última atualização de infetados e mortes em Congo-Quinxassa?
    - action_search_stats_municipal
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Salvaterra de Magos"}
    - slot{"country_municipal_confirmed_accum": 10}
    - utter_country_municipal_hasdata

## pt_covid_situation_infected_municipa2
* pt_covid_situation_last_update: Atualização em Amarante
    - action_search_stats_municipal
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Salvaterra de Magos"}
    - slot{"country_municipal_confirmed_accum": 10}
    - utter_country_municipal_hasdata

    ## pt_covid_situation_infected_region_notOk
* pt_covid_situation_infected: Quantos casos de infetados ativos há em Mann?
  - action_search_stats_region
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

## pt_covid_situation_infected_region_empty
* pt_covid_situation_infected: casos no total confirmados em Japan
  - action_search_stats_region
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

## pt_covid_situation_infected_region_empty2
* pt_covid_situation_last_update: Atualização em Lamego
    - action_search_stats_region
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Centro"}
    - slot{"country_region_confirmed_accum": 8}
    - utter_country_region_hasdata
* pt_covid_situation_last_update: Novos casos e mortes em República da Indonésia?
    - action_search_stats_region
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

## pt_covid_situation_infected_region_notOk
* pt_covid_situation_infected: Contagem infectada ativa em Mortágua
  - action_search_stats_region
  - slot{"country_region_search_successful": "not-ok"}
  - utter_country_municipal_nodata
* pt_vocative_no: Nem por isso.
  - utter_pt_further_questions

## pt_covid_situation_infected_region_empty
* pt_covid_situation_infected: Contagem infectados no total em Pombal
  - action_search_stats_region
  - slot{"country_region_search_successful": "not-ok"}
  - utter_country_municipal_nodata
* pt_vocative_no: nada
  - utter_pt_further_questions


## pt_covid_situation_infected_region2
* pt_covid_situation_last_update: Últimos dados de Macedo de Cavaleiros
    - action_search_stats_municipal
    - slot{"country_municipal_search_successful": "ok"}
    - slot{"country_municipal": "Madeira"}
    - slot{"country_municipal_confirmed_accum": 10}
    - utter_country_region_hasdata


## pt_covid_situation_region_municipal_country_mixed
* pt_covid_situation: Quantos casos existem em Marinha Grande?
    - slot{"pt_country_municipal": "Ribeira Brava"}
    - action_search_stats_municipal
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
* pt_covid_situation: Quantos casos existem em Porto?
    - slot{"pt_country_region": "Centro"}
    - action_search_stats_region
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Centro"}
    - slot{"country_region_confirmed_accum": 3569}
    - utter_country_region_hasdata
## pt_quarantine_general
* pt_quarantine_general: O que é o isolamento profilático?
  - utter_pt_quarantine_general

## pt_prevention_medical_attention
* pt_prevention_medical_attention: Caso apresente algum destes, o que devo fazer ?
  - utter_pt_prevention_medical_attention

## pt_prevention_informed
* pt_prevention_informed: Devo me manter informado?
  - utter_pt_prevention_informed

## pt_cc_fun_fact
* pt_cc_fun_fact: Conta-me um fato interessante
  - utter_pt_cc_fun_fact

## pt_economy_consequences
* pt_economy_consequences: Quais são as consequências do COVID-19 na Economia?
  - utter_pt_economy_consequences

## pt_stayhomeinfo_supermarket
* pt_stayhomeinfo_supermarket: Que cuidados devo ter no supermercado
  - utter_pt_stayhomeinfo_supermarket

## pt_bot_sports
* pt_bot_sports: Relação com desporto.
  - utter_pt_bot_sports

## pt_user_no_data
* pt_user_no_data: Esqueci-me dos meus documentos.
  - utter_pt_user_no_data

## pt_bot_games
* pt_bot_games: Tu gostas de jogos de computador?
  - utter_pt_bot_games

## pt_deconfinement_establishments
* pt_deconfinement_establishments: Fases do plano de desconfinamento
  - utter_pt_deconfinement_establishments

## pt_state_calamity
* pt_state_calamity: Calamidade pública
  - utter_pt_state_calamity

## pt_spread_phases
* pt_spread_phases: Em que fase de transmissão estamos atualmente?
  - utter_pt_spread_phases

## pt_bot_sing
* pt_bot_sing: Tens jeito para cantar?
  - utter_pt_bot_sing

## pt_bot_personal_questions
* pt_bot_personal_questions: Where do you go after work?
  - utter_pt_bot_personal_questions

## pt_user_laugh
* pt_user_laugh: haha
  - utter_pt_user_laugh

## pt_portugal_elders
* pt_portugal_elders: idosos podem sair de casa?
  - utter_pt_portugal_elders

## pt_bot_worst_experience
* pt_bot_worst_experience: Diz a tua pior experiência.
  - utter_pt_bot_worst_experience

## pt_cc_deepest_point
* pt_cc_deepest_point: Qual será o sítio mais profundo no planeta
  - utter_pt_cc_deepest_point

## pt_cc_geography
* pt_cc_geography: A Holanda tem montanhas?
  - utter_pt_cc_geography

## pt_covid_sex
* pt_covid_sex: Relações sexuais e covid
  - utter_pt_covid_sex

## pt_spread_washing_clothes
* pt_spread_washing_clothes: A que temperatura devo lavar a roupa?
  - utter_pt_spread_washing_clothes

## pt_cc_highest_building
* pt_cc_highest_building: Qual é o maior edifício da terra
  - utter_pt_cc_highest_building

## pt_state_emergency_end
* pt_state_emergency_end: até quando durará o estado de emergência em Portugal?
  - utter_pt_state_emergency_end

## pt_covid_ibuprofen
* pt_covid_ibuprofen: Ibuprofen
  - utter_pt_covid_ibuprofen

## carousel-trigger
* carousel-trigger: 
  - utter_carousel_trigger

## video-trigger
* video-trigger: 
  - utter_video_trigger

## cms-trigger
* cms-trigger: 
  - utter_cms_trigger
