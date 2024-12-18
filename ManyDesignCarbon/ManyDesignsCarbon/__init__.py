
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'ManyDesignsCarbon'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 20
    C = cu(0)
    TAX = cu(0)
    ENDOWMENT = cu(14000)
    OIL_FREE_COST = cu(13000)
    BID_MAX_THRESHOLD = 10000
    BONUS_MAX_POINTS = 350000
    BONUS = 2
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    age = models.IntegerField(label='What is your age', max=125, min=13)
    gender = models.StringField(choices=[['Male', 'Male'], ['Female', 'Female']], label='What is your gender', widget=widgets.RadioSelect)
    oil_price_desicion_round = models.CurrencyField()
    alternative_cost = models.CurrencyField(initial=C.OIL_FREE_COST)
    bid_for_oil = models.CurrencyField(label='Please indicate how much you will be willing to pay for the OIL option.', max=10000, min=0)
    random_threshold = models.CurrencyField()
    purchase_oil = models.BooleanField()
    oil_cost_t0 = models.CurrencyField()
    oil_cost_t1 = models.CurrencyField()
    oil_cost_t2 = models.CurrencyField()
    oil_cost_t3 = models.CurrencyField()
    oil_cost_t4 = models.CurrencyField()
    oil_price_t0 = models.CurrencyField()
    oil_price_t1 = models.CurrencyField()
    oil_price_t2 = models.CurrencyField()
    oil_price_t3 = models.CurrencyField()
    oil_price_t4 = models.CurrencyField()
    total_oil_price = models.CurrencyField()
    is_control = models.BooleanField()
    forgone_payoff = models.CurrencyField()
    support_carbon_pricing = models.BooleanField(label='Would you be willing to take action to support carbon pricing and reduce carbon footprints?')
    willing_to_sign_petition = models.BooleanField(label='Would you be willing to sign a petition in support of carbon pricing and long-term pricing certainty?')
    clicked_petition = models.BooleanField(initial=False)
def set_payoffs(player: Player):
    import random
    
    player.random_threshold = random.randint(0, C.BID_MAX_THRESHOLD)
    
    player.purchase_oil = player.bid_for_oil >= player.random_threshold
    oil_profit = C.ENDOWMENT*5 - (player.bid_for_oil*5) - (player.total_oil_price)
    oil_free_profit = C.ENDOWMENT*5 - (C.OIL_FREE_COST*5)
    
    if player.purchase_oil:
        player.payoff = oil_profit
        player.forgone_payoff = oil_free_profit
    else:
        player.payoff = oil_free_profit
        player.forgone_payoff = oil_profit
    
def setoil_prices(player: Player):
    oil_costs_from_csv(player)
    
    if player.is_control:
        player.oil_price_t0 = player.oil_cost_t0 + C.TAX
        player.oil_price_t1 = player.oil_cost_t1 + C.TAX
        player.oil_price_t2 = player.oil_cost_t2 + C.TAX
        player.oil_price_t3 = player.oil_cost_t3 + C.TAX
        player.oil_price_t4 = player.oil_cost_t4 + C.TAX
    else:
        player.oil_price_t0 = player.oil_cost_t0 + C.TAX
        player.oil_price_t1 = player.oil_price_t0
        player.oil_price_t2 = player.oil_price_t0
        player.oil_price_t3 = player.oil_price_t0
        player.oil_price_t4 = player.oil_price_t0
    
    player.oil_price_desicion_round = player.oil_price_t0
    player.total_oil_price = player.oil_price_t0 + player.oil_price_t1 + player.oil_price_t2 + player.oil_price_t3 + player.oil_price_t4
def oil_costs_from_csv(player: Player):
    import csv
        # CSV content as a multi-line string
    csv_content = """
    date    CrudeOilClosePrice
    27/02/2015    49.76
    31/03/2015    47.6
    30/04/2015    59.63
    29/05/2015    60.3
    30/06/2015    59.47
    31/07/2015    47.12
    31/08/2015    49.2
    30/09/2015    45.09
    30/10/2015    46.59
    30/11/2015    41.65
    31/12/2015    37.04
    29/01/2016    33.62
    29/02/2016    33.75
    31/03/2016    38.34
    29/04/2016    45.92
    31/05/2016    49.1
    30/06/2016    48.33
    29/07/2016    41.6
    31/08/2016    44.7
    30/09/2016    48.24
    31/10/2016    46.86
    30/11/2016    49.44
    30/12/2016    53.72
    31/01/2017    52.81
    28/02/2017    54.01
    31/03/2017    50.6
    28/04/2017    49.33
    31/05/2017    48.32
    30/06/2017    46.04
    31/07/2017    50.17
    31/08/2017    47.23
    29/09/2017    51.67
    31/10/2017    54.38
    30/11/2017    57.4
    29/12/2017    60.42
    31/01/2018    64.73
    28/02/2018    61.64
    29/03/2018    64.94
    30/04/2018    68.57
    31/05/2018    67.04
    29/06/2018    74.15
    31/07/2018    68.76
    31/08/2018    69.8
    28/09/2018    73.25
    31/10/2018    65.31
    30/11/2018    50.93
    31/12/2018    45.41
    31/01/2019    53.79
    28/02/2019    57.22
    29/03/2019    60.14
    30/04/2019    63.91
    31/05/2019    53.5
    28/06/2019    58.47
    31/07/2019    58.58
    30/08/2019    55.1
    30/09/2019    54.07
    31/10/2019    54.18
    29/11/2019    55.17
    31/12/2019    61.06
    31/01/2020    51.56
    28/02/2020    44.76
    31/03/2020    20.48
    30/04/2020    18.84
    29/05/2020    35.49
    30/06/2020    39.27
    31/07/2020    40.27
    31/08/2020    42.61
    30/09/2020    40.22
    30/10/2020    35.79
    30/11/2020    45.34
    31/12/2020    48.52
    29/01/2021    52.2
    26/02/2021    61.5
    31/03/2021    59.16
    30/04/2021    63.58
    28/05/2021    66.32
    30/06/2021    73.47
    30/07/2021    73.95
    31/08/2021    68.5
    30/09/2021    75.03
    29/10/2021    83.57
    30/11/2021    66.18
    31/12/2021    75.21
    31/01/2022    88.15
    28/02/2022    95.72
    31/03/2022    100.28
    29/04/2022    104.69
    31/05/2022    114.67
    30/06/2022    109.5467
    29/07/2022    98.62
    31/08/2022    89.2
    30/09/2022    79.49
    31/10/2022    86.18
    30/11/2022    80.55
    30/12/2022    80.51
    31/01/2023    78.87
    28/02/2023    77.05
    31/03/2023    75.67
    28/04/2023    76.78
    31/05/2023    67.69
    """
    
    # Replace multiple spaces with a single tab
    normalized_content = "\n".join(["\t".join(line.split()) for line in csv_content.strip().split("\n")])
    
    # Debug: Print headers
    rows = list(csv.DictReader(csv_content.strip().split("\n"), delimiter="\t"))
    #print("Headers:", rows[0].keys())  # Debugging step to check column names
    
    # Parse the normalized content
    rows = list(csv.DictReader(normalized_content.split("\n"), delimiter="\t"))
    
    # Extract prices
    prices = [row["CrudeOilClosePrice"] for row in rows]
    
    
    if player.field_maybe_none('oil_cost_t0') is None:
        semi_rounds_number = (player.round_number - 1) * 5
        player.oil_cost_t0 = float(prices[semi_rounds_number ])*100
        player.oil_cost_t1 = float(prices[semi_rounds_number  + 1])*100
        player.oil_cost_t2 = float(prices[semi_rounds_number  + 2])*100
        player.oil_cost_t3 =  float(prices[semi_rounds_number  + 3])*100
        player.oil_cost_t4 =  float(prices[semi_rounds_number  + 4])*100
    else:  # in case it gets called twice in the Desicion.html to get a list of all prices per period
        return prices
    
    
def setup_player(player: Player):
    session = player.session
    player.is_control = session.config['is_control']
    
    
class Introduction(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        setup_player(player)
        return player.round_number == 1
class Desicion(Page):
    form_model = 'player'
    form_fields = ['bid_for_oil']
    @staticmethod
    def vars_for_template(player: Player):
        setup_player(player)
        setoil_prices(player)
        
        html_table = ""
        prices = oil_costs_from_csv(player)
        periods = None
        
        if player.round_number > 1:
            periods = list(range(5*(player.round_number-1) - 1, -1, -1))  # 4,3,2,1,0
        
            html_table += '''
            <br>In the table below, is the history of the oil prices and your choices
        <tr>
            <th>Period Number</th>
            <th>OIL Cost</th>
            <th>OIL-FREE Cost</th>
            <th>Your bid</th>
            <th>The option you bought and its cost</th>
            <th>Endowment</th>
            <th>Your Score</th>
        </tr>
            '''
        
            for r in periods:
                desicion_round = r%5 == 0
                pl = player.in_round((r//5) + 1)
                oil_cost = (100*float(prices[r]) if pl.is_control else pl.oil_price_desicion_round)
                oil_profit = C.ENDOWMENT - pl.bid_for_oil - oil_cost
                oil_free_profit = C.ENDOWMENT - C.OIL_FREE_COST
        
                html_table += ('<tr style="font-weight: bold; background-color: Gainsboro;">' if desicion_round else '<tr>') 
                html_table += "<td>" + str(r) + (' <i>(Desicion Round)</i>' if desicion_round else '') +"</td>"  #period
                html_table += '<td' + (' style="color: DimGray;">' if not pl.is_control and not desicion_round else '>') + str(int(100*float(prices[r]))) + "</td>"  # oil cost
                html_table += "<td>" + str(int(C.OIL_FREE_COST)) + "</td>"  # oil-free cost
                html_table += '<td' + (' style="text-decoration: line-through;"' if not pl.purchase_oil else '') + '>' + (str(int(pl.bid_for_oil)) + "" if desicion_round else '') +"</td>"  #bid
                html_table += "<td>" + ('<i>OIL:</i> ' + str(int(oil_cost)) + ' + Your bid = ' + str(int(float(oil_cost)+float(pl.bid_for_oil))) if pl.purchase_oil else '<i>OIL-FREE:</i> '+ str(int(C.OIL_FREE_COST)) +' Points') + "</td>"  # your choice
                html_table += "<td>" + str(int(C.ENDOWMENT)) + "</td>"  # Endowment
                html_table += '<td style="font-weight: bold;">' + (str(int(oil_profit)) if pl.purchase_oil else str(int(oil_free_profit))) + "</td>"  # Your Score
        
        
                html_table += "</tr>"
        
        
        return dict(
            html_table=html_table,
        )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoffs(player)
class Result(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        # for html table
        html_table = ""
        
        prices = oil_costs_from_csv(player)
        periods = list(range(5*(player.round_number)-1, 5*(player.round_number-1) - 1, -1))  # r=2: 9,8,7,6,5
        periods.reverse()
        
        
        # for info
        oil_free_profit = C.ENDOWMENT - C.OIL_FREE_COST
        avg_gain = float(player.payoff)/5
        avg_gain_ifnotax = 0
        desicion_round_gain = None
        player.purchase_oil = player.bid_for_oil >= player.random_threshold
        if player.purchase_oil:
            desicion_round_gain = C.ENDOWMENT - player.bid_for_oil - player.oil_price_desicion_round
        else:
            desicion_round_gain = C.ENDOWMENT - C.OIL_FREE_COST
        
        
        html_table += '''
        <br>In the table below, are your earnings for that desicion
        <tr>
            <th>Period Number</th>
            <th>OIL Cost</th>
            <th>OIL-FREE Cost</th>
            <th>Your bid</th>
            <th>The option you bought and its price</th>
            <th>Endowment</th>
            <th>Your Score</th>
        </tr>
            '''
        
        for r in periods:
            desicion_round = r%5 == 0
            pl = player.in_round((r//5) + 1)
            oil_cost = (100*float(prices[r]) if pl.is_control else pl.oil_price_desicion_round)
            oil_profit = C.ENDOWMENT - pl.bid_for_oil - oil_cost
            oil_free_profit = C.ENDOWMENT - C.OIL_FREE_COST

            avg_gain_ifnotax += C.ENDOWMENT - pl.bid_for_oil - 100*float(prices[r])
        
            html_table += ('<tr style="font-weight: bold; background-color: Gainsboro;">' if desicion_round else '<tr>') 
            html_table += "<td>" + str(r) + (' <i>(Desicion Round)</i>' if desicion_round else '') +"</td>"  #period
            html_table += "<td" + (' class="no"' if not pl.purchase_oil else '') + (' style="color: Blue Gray;"' if pl.is_control and not desicion_round else '') + '>' + str(int(100*float(prices[r]))) + "</td>"  # oil cost
            html_table += "<td" + (' class="no"' if pl.purchase_oil else '') + '>' + str(int(C.OIL_FREE_COST)) + "</td>"  # oil-free cost
            html_table += "<td" + (' class="no"' if not pl.purchase_oil else '') + '>' + (str(int(pl.bid_for_oil)) if desicion_round else '') +"</td>"  #bid
        
            html_table += "<td>" + ('<i>OIL:</i> ' + str(int(oil_cost)) + ' + Your bid = ' + str(int(float(oil_cost)+float(pl.bid_for_oil))) if pl.purchase_oil else '<i>OIL-FREE:</i> '+ str(int(C.OIL_FREE_COST)) +' Points') + "</td>"  # your choice
            html_table += "<td>" + str(int(C.ENDOWMENT)) + "</td>"  # Endowment
            html_table += '<td style="font-weight: bold;">' + (str(int(oil_profit)) if pl.purchase_oil else str(int(oil_free_profit))) + "</td>"  # Your Score
        
        
            html_table += "</tr>"
        
        return dict(
            html_table=html_table,
            avg_gain = avg_gain,
            avg_gain_ifnotax = (avg_gain_ifnotax/5),
            desicion_round_gain=desicion_round_gain,
            oil_free_profit=oil_free_profit,
        )
class EndGame(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        #set player set initial values and call it in each round (including introduction)
        return player.round_number == C.NUM_ROUNDS

    def vars_for_template(player: Player):
        session = player.session
        participant = player.participant
        # sum score
        total_score = 0
        for pl in player.in_all_rounds():
            total_score += pl.payoff
        
        # set payoff for bonus calculation
        participant.payoff=1000*(20/C.NUM_ROUNDS)*C.BONUS*total_score/C.BONUS_MAX_POINTS
        total_payoff=participant.payoff_plus_participation_fee()
        
        #values for display
        bonus=total_payoff-session.config['participation_fee']
        return dict(
            total_score=total_score,
            total_payoff=total_payoff,
            bonus=bonus,
        )
class Petition(Page):
    form_model = 'player'
    form_fields = ['support_carbon_pricing', 'willing_to_sign_petition', 'clicked_petition']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
    def vars_for_template(player: Player):
        control_petition_link = "https://www.change.org/p/fair-and-stable-carbon-pricing-mechanisms-22acf600-ec5a-4c56-bc75-6f4eb3045b58"
        treatement_petition_link = "https://www.change.org/p/fair-and-stable-carbon-pricing-mechanisms-8d011180-2449-4531-aa6a-46bd7e8b0dda"
        link = (control_petition_link if player.is_control else treatement_petition_link)
        return dict(
            link = link,
        )

page_sequence = [Introduction, Desicion, Result, EndGame, Petition]