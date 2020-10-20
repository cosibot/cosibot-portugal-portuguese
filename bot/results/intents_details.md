# Intents
|               class                |support|f1-score|                        confused_with                         |
|------------------------------------|------:|-------:|--------------------------------------------------------------|
|pt_covid_info                       |    611|   0.999|N/A                                                           |
|pt_covid_situation                  |    463|   0.997|pt_covid_situation_infected(1), pt_covid_current_statistics(1)|
|pt_covid_situation_infected         |    459|   0.999|N/A                                                           |
|pt_covid_situation_last_update      |    386|   1.000|N/A                                                           |
|pt_covid_sars                       |    316|   1.000|N/A                                                           |
|pt_country                          |    247|   0.998|pt_quarantine_general(1)                                      |
|pt_cc_philosophical                 |    183|   0.989|pt_cc_weather(1), pt_user_love(1)                             |
|pt_covid_incubation                 |    175|   1.000|N/A                                                           |
|pt_spread_no_symptoms               |    160|   1.000|N/A                                                           |
|pt_cc_religion                      |    140|   0.996|N/A                                                           |
|pt_spread_pets                      |    140|   1.000|N/A                                                           |
|pt_covid_meaning                    |    132|   1.000|N/A                                                           |
|pt_comment_offense                  |    129|   0.960|pt_comment_negative(8), pt_vocative_call(1)                   |
|pt_prevention_medicine              |    125|   0.996|N/A                                                           |
|pt_covid_situation_infected_critical|    118|   1.000|N/A                                                           |
|pt_features_date                    |     96|   1.000|N/A                                                           |
|pt_spread_general                   |     89|   1.000|N/A                                                           |
|pt_prevention_medical_attention     |     81|   0.987|pt_covid_aftereffects_immunity(1), pt_prevention_home(1)      |
|pt_bot_personal_questions           |     81|   0.988|pt_user_friend(1)                                             |
|pt_features_time                    |     79|   1.000|N/A                                                           |
|pt_user_no_further_questions        |     73|   0.943|pt_vocative_thank_you(4), pt_comment_negative(3)              |
|pt_vocative_thank_you               |     72|   0.959|pt_comment_positive(2)                                        |
|pt_greeting_goodbye                 |     69|   0.985|pt_user_no_further_questions(1), pt_greeting_hello(1)         |
|pt_user_no_data                     |     68|   1.000|N/A                                                           |
|pt_covid_surfaces                   |     66|   1.000|N/A                                                           |
|pt_bot_games                        |     61|   1.000|N/A                                                           |
|pt_prevention_touch                 |     60|   0.992|N/A                                                           |
|pt_prevention_respiratory_hygiene   |     59|   1.000|N/A                                                           |
|pt_covid_preexisting_illness        |     59|   1.000|N/A                                                           |
|pt_bot_appearance                   |     57|   0.982|pt_bot_real(1), pt_spread_washing_clothes(1)                  |
|pt_covid_worry                      |     56|   0.991|pt_bot_fear(1)                                                |
|pt_covid_symptoms                   |     55|   1.000|N/A                                                           |
|pt_mask_general                     |     55|   1.000|N/A                                                           |
|pt_cc_weather                       |     54|   0.991|N/A                                                           |
|pt_spread_risk                      |     53|   1.000|N/A                                                           |
|pt_bot_sports                       |     53|   1.000|N/A                                                           |
|pt_cc_politics                      |     53|   1.000|N/A                                                           |
|pt_mask_use_put                     |     53|   1.000|N/A                                                           |
|pt_cc_joke                          |     52|   0.937|N/A                                                           |
|pt_prevention_general               |     52|   1.000|N/A                                                           |
|pt_user_happy                       |     52|   0.981|N/A                                                           |
|pt_cc_highest_building              |     52|   1.000|N/A                                                           |
|pt_comment_positive                 |     51|   0.952|pt_comment_smart(1)                                           |
|pt_cc_deepest_point                 |     50|   1.000|N/A                                                           |
|pt_prevention_clean_hands           |     49|   1.000|N/A                                                           |
|pt_bot_worst_experience             |     48|   1.000|N/A                                                           |
|pt_user_love                        |     48|   0.990|N/A                                                           |
|pt_comment_racist                   |     47|   1.000|N/A                                                           |
|pt_comment_negative                 |     44|   0.837|pt_vocative_yes(1), pt_cc_joke(1)                             |
|pt_cc_geography                     |     44|   0.989|pt_covid_situation(1)                                         |
|pt_bot_languages                    |     44|   1.000|N/A                                                           |
|pt_covid_situation_tested           |     44|   0.989|pt_test_per_day(1)                                            |
|pt_covid_situation_recovered        |     43|   1.000|N/A                                                           |
|pt_travel_while                     |     41|   0.975|pt_travel_before(2)                                           |
|pt_vocative_sorry                   |     41|   1.000|N/A                                                           |
|pt_greeting_hello                   |     41|   0.907|pt_greeting_how_are_you(2)                                    |
|pt_bot_books                        |     41|   0.976|N/A                                                           |
|pt_comment_smart                    |     41|   0.988|N/A                                                           |
|pt_vocative_yes                     |     40|   0.975|pt_greeting_hello(1)                                          |
|pt_coronavirus_info                 |     39|   0.987|pt_covid_info(1)                                              |
|pt_bot_real                         |     39|   0.987|N/A                                                           |
|pt_vocative_call                    |     37|   0.933|pt_comment_negative(1), pt_bot_books(1)                       |
|pt_spread_air                       |     37|   1.000|N/A                                                           |
|pt_travel_before                    |     37|   0.961|N/A                                                           |
|pt_cc_chicken_egg                   |     37|   1.000|N/A                                                           |
|pt_bot_capabilities                 |     37|   0.919|pt_comment_negative(1), pt_vocative_help(1)                   |
|pt_greeting_how_are_you             |     36|   0.914|pt_greeting_hello(4)                                          |
|pt_bot_residence                    |     35|   0.944|pt_bot_personal_questions(1)                                  |
|pt_cc_fun_fact                      |     35|   1.000|N/A                                                           |
|pt_vocative_help                    |     34|   0.971|pt_bot_capabilities(1)                                        |
|pt_user_friend                      |     34|   0.971|N/A                                                           |
|pt_bot_availability                 |     34|   1.000|N/A                                                           |
|pt_mask_use_after                   |     33|   1.000|N/A                                                           |
|pt_spread_feces                     |     33|   1.000|N/A                                                           |
|pt_bot_origin                       |     33|   0.952|pt_bot_residence(3)                                           |
|pt_prevention_home                  |     33|   0.985|N/A                                                           |
|pt_bot_hobbies                      |     33|   1.000|N/A                                                           |
|pt_bot_music                        |     32|   1.000|N/A                                                           |
|pt_travel_after                     |     32|   0.984|pt_travel_before(1)                                           |
|pt_bot_fear                         |     32|   0.955|N/A                                                           |
|pt_bot_name                         |     32|   1.000|N/A                                                           |
|pt_vocative_no                      |     31|   1.000|N/A                                                           |
|pt_user_angry                       |     31|   0.967|pt_user_happy(2)                                              |
|pt_spread_animals                   |     31|   0.984|pt_bot_capabilities(1)                                        |
|pt_bot_sing                         |     31|   1.000|N/A                                                           |
|pt_bot_goal                         |     30|   0.983|pt_bot_capabilities(1)                                        |
|pt_bot_version                      |     29|   1.000|N/A                                                           |
|pt_cc_newspaper                     |     29|   1.000|N/A                                                           |
|pt_covid_situation_deaths           |     28|   1.000|N/A                                                           |
|pt_user_laugh                       |     28|   0.880|pt_cc_joke(6)                                                 |
|pt_cc_lets_talk                     |     27|   0.981|pt_vocative_call(1)                                           |
|pt_bot_movies                       |     27|   0.981|pt_bot_books(1)                                               |
|pt_user_scared                      |     27|   0.962|pt_bot_fear(2)                                                |
|pt_prevention_informed              |     26|   1.000|N/A                                                           |
|pt_prevention_distance              |     25|   1.000|N/A                                                           |
|pt_covid_aftereffects_immunity      |     25|   0.980|N/A                                                           |
|pt_bot_sexual                       |     23|   1.000|N/A                                                           |
|pt_cc_moon                          |     23|   1.000|N/A                                                           |
|pt_covid_current_statistics         |     21|   0.977|N/A                                                           |
|pt_bot_personality                  |     18|   0.941|pt_comment_positive(2)                                        |
|pt_user_particles                   |     18|   1.000|N/A                                                           |
|pt_prevention_measures              |     18|   1.000|N/A                                                           |
|pt_covid_sex                        |     17|   1.000|N/A                                                           |
|pt_state_emergency_end              |     16|   1.000|N/A                                                           |
|pt_sources                          |     13|   0.960|pt_prevention_touch(1)                                        |
|pt_prevention_entering_home         |     13|   1.000|N/A                                                           |
|pt_vocative_you_welcome             |     13|   1.000|N/A                                                           |
|pt_myth_packages                    |     13|   1.000|N/A                                                           |
|pt_myth_alcohol                     |     12|   1.000|N/A                                                           |
|pt_quarantine_children              |     11|   1.000|N/A                                                           |
|pt_test_where                       |     11|   1.000|N/A                                                           |
|pt_news_request                     |     10|   1.000|N/A                                                           |
|pt_covid_pregnancy                  |     10|   1.000|N/A                                                           |
|pt_deconfinement_establishments     |     10|   1.000|N/A                                                           |
|pt_quarantine_general               |      9|   0.947|N/A                                                           |
|pt_spread_washing_clothes           |      9|   0.947|N/A                                                           |
|pt_test_what                        |      9|   1.000|N/A                                                           |
|pt_patient_home                     |      8|   1.000|N/A                                                           |
|pt_state_calamity                   |      8|   1.000|N/A                                                           |
|pt_portugal_elders                  |      8|   1.000|N/A                                                           |
|pt_spread_surfaces_food_objects     |      8|   1.000|N/A                                                           |
|pt_covid_crisis_howlong             |      8|   1.000|N/A                                                           |
|pt_quarantine_dos_and_donts         |      8|   1.000|N/A                                                           |
|pt_test_per_day                     |      8|   0.941|N/A                                                           |
|pt_covid_ibuprofen                  |      8|   0.933|pt_prevention_medicine(1)                                     |
|start                               |      7|   1.000|N/A                                                           |
|pt_covid_mortality_rate             |      7|   1.000|N/A                                                           |
|pt_covid_pandemic                   |      6|   1.000|N/A                                                           |
|pt_portugal_rates                   |      6|   1.000|N/A                                                           |
|pt_economy_consequences             |      6|   1.000|N/A                                                           |
|pt_portugal_ill_foreigner           |      6|   1.000|N/A                                                           |
|pt_covid_babys_children             |      6|   1.000|N/A                                                           |
|pt_portugal_ill_no_covid            |      6|   1.000|N/A                                                           |
|pt_test_general                     |      5|   1.000|N/A                                                           |
|pt_covid_duration                   |      5|   1.000|N/A                                                           |
|pt_covid_alike                      |      5|   1.000|N/A                                                           |
|pt_patient_referral                 |      5|   1.000|N/A                                                           |
|pt_stayhomeinfo_supermarket         |      5|   1.000|N/A                                                           |
|pt_prevention_food                  |      4|   1.000|N/A                                                           |
|pt_prevention_gloves                |      4|   1.000|N/A                                                           |
|pt_state_emergency_info             |      4|   1.000|N/A                                                           |
|pt_portugal_government_measures     |      4|   1.000|N/A                                                           |
|pt_covid_cosibot                    |      4|   1.000|N/A                                                           |
|pt_state_emergency_run              |      4|   1.000|N/A                                                           |
|pt_covid_close_contact              |      3|   1.000|N/A                                                           |
|pt_quarantine_toiletpaper           |      3|   1.000|N/A                                                           |
|pt_covid_community_transmission     |      3|   1.000|N/A                                                           |
|pt_spread_phases                    |      3|   1.000|N/A                                                           |
|pt_myth_transmission_hot_areas      |      2|   1.000|N/A                                                           |
|pt_bot_change_bot                   |      2|   1.000|N/A                                                           |



# Confusion table
|            intent             |        confused_with         |count|
|-------------------------------|------------------------------|----:|
|pt_comment_offense             |pt_comment_negative           |    8|
|pt_user_laugh                  |pt_cc_joke                    |    6|
|pt_greeting_how_are_you        |pt_greeting_hello             |    4|
|pt_user_no_further_questions   |pt_vocative_thank_you         |    4|
|pt_bot_origin                  |pt_bot_residence              |    3|
|pt_user_no_further_questions   |pt_comment_negative           |    3|
|pt_bot_personality             |pt_comment_positive           |    2|
|pt_user_scared                 |pt_bot_fear                   |    2|
|pt_vocative_thank_you          |pt_comment_positive           |    2|
|pt_greeting_hello              |pt_greeting_how_are_you       |    2|
|pt_travel_while                |pt_travel_before              |    2|
|pt_user_angry                  |pt_user_happy                 |    2|
|pt_vocative_call               |pt_comment_negative           |    1|
|pt_comment_positive            |pt_comment_smart              |    1|
|pt_comment_negative            |pt_vocative_yes               |    1|
|pt_covid_situation             |pt_covid_current_statistics   |    1|
|pt_spread_animals              |pt_bot_capabilities           |    1|
|pt_greeting_goodbye            |pt_user_no_further_questions  |    1|
|pt_greeting_goodbye            |pt_greeting_hello             |    1|
|pt_bot_personal_questions      |pt_user_friend                |    1|
|pt_covid_situation             |pt_covid_situation_infected   |    1|
|pt_bot_appearance              |pt_spread_washing_clothes     |    1|
|pt_bot_goal                    |pt_bot_capabilities           |    1|
|pt_bot_residence               |pt_bot_personal_questions     |    1|
|pt_country                     |pt_quarantine_general         |    1|
|pt_bot_capabilities            |pt_comment_negative           |    1|
|pt_bot_capabilities            |pt_vocative_help              |    1|
|pt_covid_ibuprofen             |pt_prevention_medicine        |    1|
|pt_cc_geography                |pt_covid_situation            |    1|
|pt_bot_appearance              |pt_bot_real                   |    1|
|pt_vocative_call               |pt_bot_books                  |    1|
|pt_covid_worry                 |pt_bot_fear                   |    1|
|pt_coronavirus_info            |pt_covid_info                 |    1|
|pt_vocative_yes                |pt_greeting_hello             |    1|
|pt_comment_negative            |pt_cc_joke                    |    1|
|pt_cc_lets_talk                |pt_vocative_call              |    1|
|pt_prevention_medical_attention|pt_prevention_home            |    1|
|pt_prevention_medical_attention|pt_covid_aftereffects_immunity|    1|
|pt_cc_philosophical            |pt_user_love                  |    1|
|pt_cc_philosophical            |pt_cc_weather                 |    1|
|pt_bot_movies                  |pt_bot_books                  |    1|
|pt_travel_after                |pt_travel_before              |    1|
|pt_vocative_help               |pt_bot_capabilities           |    1|
|pt_sources                     |pt_prevention_touch           |    1|
|pt_comment_offense             |pt_vocative_call              |    1|
|pt_covid_situation_tested      |pt_test_per_day               |    1|
