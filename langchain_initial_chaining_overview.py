import random
# create a llm model
class DummyLLM:
    def __init__(self):
        print('LLM created')
    def predict(self, prompt):

        response_list = [
    'Kabul is the capital of Afghanistan',
    'Tirana is the capital of Albania',
    'Algiers is the capital of Algeria',
    'Andorra la Vella is the capital of Andorra',
    'Luanda is the capital of Angola',
    'Buenos Aires is the capital of Argentina',
    'Yerevan is the capital of Armenia',
    'Canberra is the capital of Australia',
    'Vienna is the capital of Austria',
    'Baku is the capital of Azerbaijan',
    'Nassau is the capital of Bahamas',
    'Manama is the capital of Bahrain',
    'Dhaka is the capital of Bangladesh',
    'Bridgetown is the capital of Barbados',
    'Minsk is the capital of Belarus',
    'Brussels is the capital of Belgium',
    'Belmopan is the capital of Belize',
    'Porto-Novo is the capital of Benin',
    'Thimphu is the capital of Bhutan',
    'La Paz is the administrative capital of Bolivia',
    'Sucre is the constitutional capital of Bolivia',
    'Sarajevo is the capital of Bosnia and Herzegovina',
    'Gaborone is the capital of Botswana',
    'Brasília is the capital of Brazil',
    'Bandar Seri Begawan is the capital of Brunei',
    'Sofia is the capital of Bulgaria',
    'Ouagadougou is the capital of Burkina Faso',
    'Gitega is the capital of Burundi',
    'Phnom Penh is the capital of Cambodia',
    'Yaoundé is the capital of Cameroon',
    'Ottawa is the capital of Canada',
    'Praia is the capital of Cape Verde',
    'Bangui is the capital of Central African Republic',
    'N’Djamena is the capital of Chad',
    'Santiago is the capital of Chile',
    'Beijing is the capital of China',
    'Bogotá is the capital of Colombia',
    'Moroni is the capital of Comoros',
    'Kinshasa is the capital of Democratic Republic of the Congo',
    'Brazzaville is the capital of Republic of the Congo',
    'San José is the capital of Costa Rica',
    'Zagreb is the capital of Croatia',
    'Havana is the capital of Cuba',
    'Nicosia is the capital of Cyprus',
    'Prague is the capital of Czech Republic',
    'Copenhagen is the capital of Denmark',
    'Djibouti is the capital of Djibouti',
    'Roseau is the capital of Dominica',
    'Santo Domingo is the capital of Dominican Republic',
    'Quito is the capital of Ecuador',
    'Cairo is the capital of Egypt',
    'San Salvador is the capital of El Salvador',
    'Malabo is the capital of Equatorial Guinea',
    'Asmara is the capital of Eritrea',
    'Tallinn is the capital of Estonia',
    'Mbabane is the administrative capital of Eswatini',
    'Lobamba is the legislative capital of Eswatini',
    'Addis Ababa is the capital of Ethiopia',
    'Suva is the capital of Fiji',
    'Helsinki is the capital of Finland',
    'Paris is the capital of France',
    'Libreville is the capital of Gabon',
    'Banjul is the capital of Gambia',
    'Tbilisi is the capital of Georgia',
    'Berlin is the capital of Germany',
    'Accra is the capital of Ghana',
    'Athens is the capital of Greece',
    'St. George’s is the capital of Grenada',
    'Guatemala City is the capital of Guatemala',
    'Conakry is the capital of Guinea',
    'Bissau is the capital of Guinea-Bissau',
    'Georgetown is the capital of Guyana',
    'Port-au-Prince is the capital of Haiti',
    'Tegucigalpa is the capital of Honduras',
    'Budapest is the capital of Hungary',
    'Reykjavík is the capital of Iceland',
    'New Delhi is the capital of India',
    'Jakarta is the capital of Indonesia',
    'Tehran is the capital of Iran',
    'Baghdad is the capital of Iraq',
    'Dublin is the capital of Ireland',
    'Jerusalem is the capital of Israel',
    'Rome is the capital of Italy',
    'Kingston is the capital of Jamaica',
    'Tokyo is the capital of Japan',
    'Amman is the capital of Jordan',
    'Nur-Sultan is the capital of Kazakhstan',
    'Nairobi is the capital of Kenya',
    'Tarawa is the capital of Kiribati',
    'Pristina is the capital of Kosovo',
    'Kuwait City is the capital of Kuwait',
    'Bishkek is the capital of Kyrgyzstan',
    'Vientiane is the capital of Laos',
    'Riga is the capital of Latvia',
    'Beirut is the capital of Lebanon',
    'Maseru is the capital of Lesotho',
    'Monrovia is the capital of Liberia',
    'Tripoli is the capital of Libya',
    'Vaduz is the capital of Liechtenstein',
    'Vilnius is the capital of Lithuania',
    'Luxembourg is the capital of Luxembourg',
    'Antananarivo is the capital of Madagascar',
    'Lilongwe is the capital of Malawi',
    'Kuala Lumpur is the capital of Malaysia',
    'Malé is the capital of Maldives',
    'Bamako is the capital of Mali',
    'Valletta is the capital of Malta',
    'Majuro is the capital of Marshall Islands',
    'Nouakchott is the capital of Mauritania',
    'Port Louis is the capital of Mauritius',
    'Mexico City is the capital of Mexico',
    'Chisinau is the capital of Moldova',
    'Monaco is the capital of Monaco',
    'Ulaanbaatar is the capital of Mongolia',
    'Podgorica is the capital of Montenegro',
    'Rabat is the capital of Morocco',
    'Maputo is the capital of Mozambique',
    'Naypyidaw is the capital of Myanmar',
    'Windhoek is the capital of Namibia',
    'Yaren is the capital of Nauru (de facto)',
    'Kathmandu is the capital of Nepal',
    'Amsterdam is the capital of Netherlands',
    'Wellington is the capital of New Zealand',
    'Managua is the capital of Nicaragua',
    'Niamey is the capital of Niger',
    'Abuja is the capital of Nigeria',
    'Pyongyang is the capital of North Korea',
    'Skopje is the capital of North Macedonia',
    'Oslo is the capital of Norway',
    'Muscat is the capital of Oman',
    'Islamabad is the capital of Pakistan',
    'Ngerulmud is the capital of Palau',
    'Panama City is the capital of Panama',
    'Port Moresby is the capital of Papua New Guinea',
    'Asunción is the capital of Paraguay',
    'Lima is the capital of Peru',
    'Manila is the capital of Philippines',
    'Warsaw is the capital of Poland',
    'Lisbon is the capital of Portugal',
    'Doha is the capital of Qatar',
    'Bucharest is the capital of Romania',
    'Moscow is the capital of Russia',
    'Kigali is the capital of Rwanda',
    'Basseterre is the capital of Saint Kitts and Nevis',
    'Castries is the capital of Saint Lucia',
    'Kingstown is the capital of Saint Vincent and the Grenadines',
    'Apia is the capital of Samoa',
    'San Marino is the capital of San Marino',
    'São Tomé is the capital',]

        return {'response': random.choice(response_list)}

# create a prompt
class DummyPromptTemplate:
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
    
    def format(self,input_dict):
        return self.template.format(**input_dict)
    

template=DummyPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length','topic']
)

prompt=template.format({'length':'short','topic':'india'})

llm = DummyLLM()

llm_response = llm.predict(prompt)

print(llm_response)

# {'response': 'Nairobi is the capital of Kenya'}

# create a chain
class DummyLLMChain:

  def __init__(self, llm, prompt):
    self.llm = llm
    self.prompt = prompt

  def run(self, input_dict):

    final_prompt = self.prompt.format(input_dict)
    result = self.llm.predict(final_prompt)

    return result['response']


llm_chain = DummyLLMChain(llm,template)

llm_response = llm_chain.run({'length':'short','topic':'india'})

print(llm_response)
# Warsaw is the capital of Poland