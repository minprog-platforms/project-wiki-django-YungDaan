# Procesboek

## Wiki 🌍

Het duurde even om de inhoud van de distribution code te begrijpen en hoe alle mappen en files werkten en hoe het in elkaar zat. Zo ben ik erachter gekomen dat de map wiki dus de root project is en dat entries de bestanden bevat die we willen laten zien in mijn wikipedia implementatie. De map waarin gewerkt wordt en waar alle bestanden in komen te staan is encyclopedia.

Hierna begon ik te kijken en te ontdekken hoe alle bestanden in de map encyclopedia werkten en wat hier precies in moest en wat de voor geschreven code precies deed en of ik hier iets aan toe moet voegen in een later stadia of het zo te laten. Bijvoorbeeld in de [views.py](http://views.py) dat de voorgeschreven code door de list met entries heen gaat om de content in entries weer te geven op de wiki pagina.

Wat django zelf betreft had ik wat meer moeite met dit te begrijpen en heb ik het hoorcollege van Brian een stuk of drie keer moeten kijken om daadwerkelijk te begrijpen en toe te kunnen passen wat hij voor doet. Het werkte ook verwarrend dat alles door elkaar gaat en veel files in elkaar verwerkt moeten worden, hierdoor moest ik vaker dingen herhalen en terug kijken. Veel trail and error omdat ik dan vergeet een file te koppelen in een andere file en dit vervolgens door krijg doormiddel van een error en niet weet hoe en wat en moet gaan rondzoeken wat veel tijd in beslag nam.

Ik liep meer tegen de python gerelateerde code aan dan het html gedeelte. Al hoewel heb ik me kapot gebeten waarom hij de entries niet laden, dit heeft een paar uur geduurd voordat ik erachter kwam wat het precies was. Het bleek dus in de href te zijn dat ik de url ‘entry’ deed waardoor hij een reverse error aangaf. Dit is een stomme denk fout en uiteindelijk deze gevonden en opgelost door de naam van mijn app “wiki” toe te voegen begreep de code waar het moest zoeken. De url heb ik daarom aangepast naar ‘wiki: entry’ kleine fout maar groot probleem.

Ook raakte ik in de knoop door een typfout in mijn convert_to_html functie die ik een hele tijd niet had gezien en erover heen aan het lezen was. Ik probeerde de convert methode van Markdown te gebruiken maar typte dus conver ipv convert en las er steeds overheen. Uiteindelijk gevonden en gefixt. Volgende keer ben ik wat oplettender.

Frustratie tolerantie werd ook getest bij het pushen en commiten op github omdat dit niet werkten met een beetje geduld heb ik dit uiteindelijk gefixt.

Na veel frustratie en trail en error is het uiteindelijk gelukt om Wiki af te maken en alles werkend te maken.

## Commerce 💸

Net zoals met project van Wiki ben ik de eerste dag begonnen met het bestand te begrijpen en wat wat is. Meer informatie opdoen en googlen wat ik niet begreep zoals de dingen die nieuw waren met de bestanden zoals models. Het college heb ik weer een keer of drie gekeken en stukken hiervan opnieuw om echt te begrijpen hoe databases werken en models.

Commerce ging mij een stuk gemakkelijker af dan Wiki. Dit komt omdat ik al met django heb gewerkt met wiki en er dus al wat ervaring mee heb ookal is dit minimaal. Er zijn veel dingen die ik herhaald heb en daardoor makkelijk uit mijn vingers kwamen en omgezet werden in code. Ik liep wel aan tegen bepaalde dingen die ik nog niet had gebruikt. Zoals de prijs en de bid functie hierbij heb ik wel een paar uren versleten omdat dit nog nieuw was en ik geen idee had hoe dit toegepast moest worden. Na veel filmpjes kijken werd het wel al een stuk duidelijker en kon ik op een gegeef moment verder met het implementeren van de Bid functie. Waar ik wel tegenaan liep toen ik mijn code ging testen is dat ik veel errors tegen kwam die ik moest fixen. Dit bleken na het fixen vooral fouten te zijn met betrekking tot het linken van bestanden en typfouten die je over het hoofd ziet omdat je te snel typt.

Ik heb veel hulp gehad aan bootstrap en w3schools, met boostrap waren er een paar handige dingen vooral wat de opmaak van de site betreft. en w3schools was handig als ik uit bepaalde code niet kon komen en voorbeelden nodig had om de code toe te kunnen passen op mijn eigen implementatie van een website met een soortgelijk probleem. Ik heb ook veel aan de notes gehad van het Harvard college hier kon ik ook nuttige informatie uithalen en toepassen op mijn commerce. Zoals de many to many relationships 

Ook heb ik op mijn hoofd lopen krabben van de csrf token. Hier heb ik tot op de ochtend van de deadline mee lopen kloten tot ik iemand ernaar liet kijken en het dus gewoon bleek te zijn dat ik {% csrf token %} neer had gezet ipv {% csrf_token %} dit krijg je er neem ik aan van als je dit soort dingen niet copy paste.

Alles werkt van commerce ik heb helaas geen tijd gehad om categorieën werkend te krijgen je kan wel items listen op categorieën maar niet sorteren op categorie hier heb ik helaas geen tijd voor gehad gelukkig was dit ook een extra taak en dus niet specifiek benodigd.