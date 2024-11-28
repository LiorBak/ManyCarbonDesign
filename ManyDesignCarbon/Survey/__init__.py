from random import choices

from otree.api import *

doc = """
Blueprint app for the policy survey of #ManyDesignsCarbon 
Programmed by: Armando Holzknecht
"""


class C(BaseConstants):
    NAME_IN_URL = 'Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # demographics_one
    age = models.IntegerField(label='What is your age?', min=0, max=100)
    gender = models.StringField(label='What is your gender?', choices = ['Female', 'Male','Other'])
    nationality = models.StringField(label='What is your nationality?',
                                     choices=['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan',
                                              'Antiguan and Barbudan', 'Argentine', 'Armenian', 'Australian',
                                              'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi',
                                              'Barbadian', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese',
                                              'Bissau-Guinean', 'Bolivian', 'Bosnian and Herzegovinian', 'Botswanan',
                                              'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese',
                                              'Burundian', 'Cabo Verdean', 'Cambodian', 'Cameroonian', 'Canadian',
                                              'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian',
                                              'Comoran', 'Congolese (Congo-Brazzaville)', 'Costa Rican', 'Croatian',
                                              'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djiboutian', 'Dominican',
                                              'Dominican (from the Dominican Republic)', 'Dutch', 'Ecuadorian',
                                              'Egyptian', 'Emirati', 'Equatorial Guinean', 'Eritrean', 'Estonian',
                                              'Eswatini', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French',
                                              'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek',
                                              'Grenadian', 'Guatemalan', 'Guinean', 'Guyanese', 'Haitian', 'Honduran',
                                              'Hungarian', 'I-Kiribati', 'Icelandic', 'Indian', 'Indonesian', 'Iranian',
                                              'Iraqi', 'Irish', 'Israeli', 'Italian', 'Jamaican', 'Japanese',
                                              'Jordanian', 'Kazakh', 'Kenyan', 'Kittitian or Nevisian', 'Kosovar',
                                              'Kuwaiti', 'Kyrgyz', 'Lao', 'Latvian', 'Lebanese', 'Lesotho', 'Liberian',
                                              'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Malagasy',
                                              'Malawian', 'Malaysian', 'Maldivian', 'Malian', 'Maltese', 'Marshallese',
                                              'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan',
                                              'Mongolian', 'Montenegrin', 'Monégasque', 'Moroccan', 'Mozambican',
                                              'Namibian', 'Nauruan', 'Nepali', 'New Zealander', 'Ni-Vanuatu',
                                              'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'North Macedonian',
                                              'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Palestinian', 'Panamanian',
                                              'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese',
                                              'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran',
                                              'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Senegalese', 'Serbian',
                                              'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovak', 'Slovenian',
                                              'Solomon Islander', 'Somali', 'South African', 'South Korean',
                                              'South Sudanese', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamese',
                                              'Swedish', 'Swiss', 'Syrian', 'Tajik', 'Tanzanian', 'Thai', 'Timorese',
                                              'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish',
                                              'Turkmen', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbek',
                                              'Vatican', 'Venezuelan', 'Vietnamese', 'Vincentian', 'Yemeni', 'Zambian',
                                              'Zimbabwean'])
    country_birth = models.StringField(label='What is your country of birth?',
                                       choices=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
                                                'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
                                                'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                                                'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
                                                'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
                                                'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon',
                                                'Canada', 'Central African Republic', 'Chad', 'Chile', 'China',
                                                'Colombia', 'Comoros', 'Congo (Congo-Brazzaville)', 'Costa Rica',
                                                'Croatia', 'Cuba', 'Cyprus', 'Czechia (Czech Republic)', 'Denmark',
                                                'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
                                                'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
                                                "Eswatini (fmr. 'Swaziland')", 'Ethiopia', 'Fiji', 'Finland', 'France',
                                                'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada',
                                                'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See',
                                                'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
                                                'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
                                                'Kazakhstan', 'Kenya', 'Kiribati', 'Korea (North)', 'Korea (South)',
                                                'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
                                                'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
                                                'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
                                                'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
                                                'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
                                                'Mozambique', 'Myanmar (formerly Burma)', 'Namibia', 'Nauru', 'Nepal',
                                                'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
                                                'North Macedonia (formerly Macedonia)', 'Norway', 'Oman', 'Pakistan',
                                                'Palau', 'Palestine State', 'Panama', 'Papua New Guinea', 'Paraguay',
                                                'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
                                                'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
                                                'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
                                                'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
                                                'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
                                                'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain',
                                                'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
                                                'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga',
                                                'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu',
                                                'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
                                                'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                                                'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
                                       )
    employment = models.StringField(label='What is your employment status?',
                                    choices = ['Employed','Unemployed','Student','Retired','Other'])

    # demographics_two
    agglomeration = models.StringField(label='Do you live in a rural or an urban area? I live in:',
                                       choices = ['a rural area', 'a small town (5,000 - 20,000 inhabitants)',
                                                  'a large town (20,000 - 50,000 inhabitants)',
                                                  'a small city or its suburbs (50,000 - 250,000 inhabitants)',
                                                  'a large city or its suburbs (250,000 - 3,000,000 inhabitants)',
                                                  'a very large city or its suburbs (more than 3 million inhabitants)'])
    children = models.StringField(label = 'How many children do you have?',
                                  choices=['0','1','2','3','4 or more'])
    education = models.StringField(label='What is the highest level of education you have completed?',
                                   choices = ['No schooling completed', 'Primary school', 'Lower secondary school',
                                              'Vocational degree', 'High school', 'College degree', "Master's degree or above"])
    income = models.StringField(label='What was the annual income of your household in 2023 (before withholding tax)?',
                                choices=['Less than $35,000', 'between $35,000 - $70,000', 'between $70,000 - $120,000',
                                         'More than $120,000'])

    # political views
    pol_orientation = models.IntegerField(label='On economic policy matters, where do you see yourself on a scale'
                                                      'from  1 to 5, where 1 is Left and 5 is Right?',
                                                choices=[[1,'Left'], [2,''], [3,''], [4,''], [5,'Right']],
                                                widget=widgets.RadioSelectHorizontal)
    pol_affiliation = models.StringField(label='What do you consider to be your political affiliation, as of today?',
                                               choices=['Republican','Democrat','Independent','Other','Non-Affiliated'])

    # private behavior
    prim_heat_source = models.StringField(label='What is the main way of heating your home?',
                                                choices=['Electricity','Gas','Heating oil','Coal','Wood, Solar, Geothermal or heat pump',
                                                         'District heating',"Don't know", 'Prefer not to say'])

    costs_gas = models.StringField(label='In a typical month, how much to you spend on gas for driving?',
                                   choices= ['Less than $5', '$5 - $25', '$25 - $75', '$75 - $125',
                                             '$125 - $175', '$175 - $225', 'More than $225'])

    flight_trips = models.StringField(label='How many round-trip flights did you take last year?',
                                      choices=['0','1','2','3 or 4','5 to 7','8 to 14', '15 or more'])
    beef_cons = models.StringField(label='How often do you eat beef?',
                                          choices = ['Never','Less than once a week','One to four times per week',
                                                     'Almost or at least daily'])

    # trust in government
    gov_trust = models.StringField(label="Do you agree or disagree with the following statement: "
                                                "\"Over the last four years, the U.S. government could generally be trusted to do what is right.\"",
                                          choices = ['Strongly disagree', 'Somewhat disagree', 'Neither agree nor disagree',
                                                     'Somewhat agree', 'Strongly agree'])

    # willingness to adopt climate friendly behavior
    limit_flying = models.StringField(label='- Limit flying',
                                      choices=['Not at all', 'A little', 'Moderately','A lot', 'A great deal'])
    limit_driving = models.StringField(label='- Limit driving',
                                      choices=['Not at all', 'A little', 'Moderately', 'A lot', 'A great deal'])
    get_evehicle = models.StringField(label='- Get an electric vehicle',
                                      choices=['Not at all', 'A little', 'Moderately', 'A lot', 'A great deal'])
    limit_beef = models.StringField(label='- Limit beef consupmtion',
                                    choices=['Not at all', 'A little', 'Moderately', 'A lot', 'A great deal'])
    limit_heating = models.StringField(label='- Limit heating',
                                       choices=['Not at all', 'A little', 'Moderately','A lot', 'A great deal'])

    #support - first page
    cp_fairness = models.StringField(label='Do you agree or disagree with the following statement: \"A <strong>carbon tax</strong> is fair.\"',
                                     choices=['Strongly disagree', 'Somewhat disagree', 'Neither agree nor disagree',
                                              'Somewhat agree', 'Strongly agree'])
    cp_support = models.StringField(label='Do you support or oppose a <strong>carbon tax in general</strong>?',
                                    choices=['Strongly oppose', 'Somewhat oppose', 'Neither support nor oppose',
                                             'Somewhat support', 'Strongly support'])
    cp_raise = models.IntegerField(label='I support <strong>raising carbon taxes</strong> on gas/fossil fuels/coal?')

    # support - second page
    sp_cp_support = models.StringField(label='Do you support or oppose <strong>a carbon tax of $120 per tonne of CO2</strong>,'
                                             ' meaning about <strong>$1 per gallon of gasoline</strong>?',
                                       choices=['Strongly oppose', 'Somewhat oppose', 'Neither support nor oppose',
                                                'Somewhat support', 'Strongly support'])
    ct_cp_support = models.StringField(label='<p>The government could use a policy called a <strong>carbon tax with cash transfers</strong>. This'
                                             ' means to compensate households for the price increases. The revenues from the '
                                             'carbon tax would be redistributed to all households, regardless of their income.</p>'
                                             '<p>Do you support or oppose <strong>a carbon tax with cash transfers in general</strong>?</p>',
                                       choices=['Strongly oppose', 'Somewhat oppose', 'Neither support nor oppose',
                                                'Somewhat support', 'Strongly support']
                                       )

    spct_cp_support = models.StringField(label='Do you support or oppose a <strong>carbon tax of $120 per tonne of CO2 (social price of '
                                               'carbon), meaning about $1.00 per gallon of gasoline <u>with cash transfers</u></strong>, whereby '
                                               'each adult would thus receive about $1500 per year?',
                                         choices=['Strongly oppose', 'Somewhat oppose', 'Neither support nor oppose',
                                                  'Somewhat support', 'Strongly support']
                                         )

    # worries
    w_droughts = models.StringField(label= ' - Severe drought and heatwaves',
                                    choices=['Very unlikely','Somewhat unlikely','Somewhat likely','Very likely'])
    w_eruptions = models.StringField(label=' - More frequent volcanic eruptions',
                                    choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'])
    w_sealevels = models.StringField(label=' - Rising sea levels',
                                    choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'])
    w_agriculture = models.StringField(label=' - Lower agricultural production',
                                    choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'])
    w_standards = models.StringField(label=' - Drop in standards of living',
                                    choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'])
    w_migration = models.StringField(label=' - Larger migration flows',
                                    choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'])
    w_conflicts = models.StringField(label=' - More armed conflicts',
                                    choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'])
    w_extinction = models.StringField(label=' - Extinction of humankind',
                                    choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'])

    # beliefs netzero and own affections
    beliefs_netzero = models.StringField(label='To what extent do you think that it is technically feasible to stop greenhouse gas '
                                               'emissions (“net-zero”) by the end of the century while maintaining satisfactory '
                                               'standards of living in the U.S.?',
                                        choices = ['Not at all', 'A little', 'Moderately', 'A lot', 'A great deal'])

    beliefs_own = models.StringField(label='To what extent do you think climate change already affects or will soon affect your '
                                           'personal life negatively?',
                                     choices=['Not at all', 'A little', 'Moderately', 'A lot', 'A great deal'])

    # beliefs in effectiveness
    effect_driving = models.StringField(label='... encourage people to drive less.',
                                        choices=['Strongly disagree', 'Somewhat disagree', 'Neither agree nor disagree',
                                                 'Somewhat agree', 'Strongly agree'])
    effect_insulation = models.StringField(label='... encourage people and companies to insulate buildings.',
                                        choices=['Strongly disagree', 'Somewhat disagree', 'Neither agree nor disagree',
                                                 'Somewhat agree', 'Strongly agree'])
    effect_fossil = models.StringField(label='... reduce the use of fossil fuels and thus greenhouse gas emissions.',
                                           choices=['Strongly disagree', 'Somewhat disagree',
                                                    'Neither agree nor disagree',
                                                    'Somewhat agree', 'Strongly agree'])
    effect_air = models.StringField(label='... reduce air pollution.',
                                       choices=['Strongly disagree', 'Somewhat disagree',
                                                'Neither agree nor disagree',
                                                'Somewhat agree', 'Strongly agree'])
    effect_economy = models.StringField(label='... have a negative effect on the U.S. economy and employment.',
                                    choices=['Strongly disagree', 'Somewhat disagree',
                                             'Neither agree nor disagree',
                                             'Somewhat agree', 'Strongly agree'])


# PAGES

class Intro(Page):
    pass

class DemographicsOne(Page):
    form_model = 'player'
    form_fields = ['age','gender','nationality','country_birth','employment']

class DemographicsTwo(Page):
    form_model = 'player'
    form_fields = ['agglomeration','children','education','income']

class Views(Page):
    form_model = 'player'
    form_fields = ['pol_orientation','pol_affiliation']

class Behavior(Page):
    form_model = 'player'
    form_fields = ['prim_heat_source','costs_gas','flight_trips','beef_cons']

class Trust(Page):
    form_model = 'player'
    form_fields = ['gov_trust']

class Adoption(Page):
    form_model = 'player'
    form_fields = ['limit_flying','limit_driving','get_evehicle','limit_beef','limit_heating']

class SupportOne(Page):
    form_model = 'player'
    form_fields = ['cp_fairness','cp_support','cp_raise']

class SPCP(Page):
    form_model = 'player'
    form_fields = ['sp_cp_support']

class CTCP(Page):
    form_model = 'player'
    form_fields = ['ct_cp_support']

class SPCTCP(Page):
    form_model = 'player'
    form_fields = ['spct_cp_support']

class Events(Page):
    form_model = 'player'
    form_fields = ['w_droughts','w_eruptions','w_sealevels','w_agriculture','w_standards','w_migration','w_conflicts','w_extinction']

class Beliefs(Page):
    form_model = 'player'
    form_fields = ['beliefs_netzero','beliefs_own']

class Effect(Page):
    form_model = 'player'
    form_fields = ['effect_driving','effect_insulation','effect_fossil','effect_air','effect_economy']

class Ending(Page):
    pass



page_sequence = [Intro, DemographicsOne, DemographicsTwo, Views, Behavior, Trust,
                 Adoption,SupportOne,SPCP, CTCP, SPCTCP, Events, Beliefs, Effect,
                 Ending]
