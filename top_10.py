# -*- coding: utf-8 -*-

from wordfreq import zipf_frequency
from wordfreq import tokenize
import spacy


from spacy_syllables import SpacySyllables
nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after="tagger")


import pandas as pd


raw_text = """
It began as a trickle of coronavirus infections as college students arrived for the fall semester. Soon that trickle became a stream, with campuses reporting dozens, and sometimes hundreds of new cases each day.
Now the stream feels like a flood. In just the past week, a New York Times survey has found, American colleges have recorded more than 36,000 additional infections, bringing the total of 88,000 cases since the pandemic began.
Not all those cases are new, and the increase is partly the result of more schools beginning to report the results of more testing. But The Times survey of 1,600 colleges also shows how widely the contagion has spread, with schools of every type and size, and in every state reporting infections.
Large outbreaks expanded on campuses as new semesters were underway.
Only about 60 of the campus cases have resulted in death — mostly of college staff — and only a small number have resulted in hospitalizations. But public health experts say the rising number also underscores an emerging reality: Colleges and universities have, as a category, become hot spots for virus transmission, much as hospitals, nursing homes and meat packing plants were earlier.
Hoping to salvage some sense of normalcy — along with lost revenue from housing fees and out-of-state tuition — many schools invested heavily in health measures to bring at least some students back to campus.
But outbreaks have forced course correction after correction.
The State University of New York at Oneonta sent students home after the virus spun out of control in less than two weeks, with more than 500 cases. And the University of Illinois at Urbana-Champaign mounted one of the most comprehensive safety plans, requiring more than 40,000 students to be tested for the virus twice a week, and barring them from campus buildings without app verification that the latest test was negative. But, some students continued partying after they received a positive test result, and hundreds were infected.
A lockdown brought the number of new cases at the university down again. But its surge pushed its metro regions toward the top of the list of U.S. areas with most cases per capita , as did spikes at universities in Oxford, Miss., and Athens, Ga.
In Des Moines, school began this week with local officials openly defying Iowa’s governor and a judge’s order by teaching remotely. The decision puts the district’s funding and administrators’ jobs at risk, and leaves students locked out of athletics and their parents uncertain whether online classes will even count.
A new study of hospital patients challenges the notion that young people are impervious. The research letter from Harvard found that among 3,222 young adults hospitalized with Covid-19, 88 died — about 2.7 percent. One in five required intensive care, and one in 10 needed a ventilator to assist with breathing. The study “establishes that Covid-19 is a life-threatening disease in people of all ages,” wrote Dr. Mitchell Katz, a deputy editor at JAMA Internal Medicine.
Public schools are obligated to teach millions of students with disabilities . But as learning moves online, many services that parents fought for are at risk.
New research suggests children in multilingual households started using their parents’ native languages more during lockdown, especially among younger kids.
Getting prisoners in Oregon out of the path of wildfires raises the risk of spreading the virus.
Officials in Oregon’s state corrections system this week began moving hundreds of inmates out of the path of the wildfires creeping toward some of their prisons. But the introduction of large groups of prisoners into different facilities may be exposing them to another risk — contracting the virus.
Juan Chavez, a lawyer with the Oregon Justice Resource Center, a nonprofit legal advocacy group, said that relocated inmates were sleeping on mattresses crammed close together, but it’s “picking your poison” between the virus and the fires. He added that he fears the relocated inmates could contribute to a superspreader event for the virus in the prisons.
But few other options exist for the Oregon Department of Corrections, which has evacuated four prisons so far.
As the Beachie Creek and Lionshead wildfires raged in an area southeast of Portland, officials hastily relocated 1,450 inmates from three prisons in Marion County — Oregon State Correctional Institution, Santiam Correctional Institution and Mill Creek Correctional Facility. Inmates were moved west, to emergency beds in the Oregon State Penitentiary in Salem on Tuesday, according to the agency.
On Thursday officials sent 1,303 inmates from Coffee Creek Correctional Facility, a prison north of Salem in Wilsonville, to the Deer Ridge Correctional Institute more than 100 miles to the southeast, said Jennifer Black, a spokeswoman for the prison system.
Those inmates were moved to avoid a third blaze, the Riverside wildfire, which is north of the Beachie Creek and Lionshead wildfires. Each of the three blazes is more than 100,000 acres in size.
Inmates will be “housed with others from their home institution whenever possible,” and officials are aware of the potential virus spread, Ms. Black said.
“We are taking all available steps to mitigate that impact,” Ms. Black said. “As we have said from the beginning, prisons were not constructed to allow for optimal social distancing.”
The virus has already ravaged the state prison population. In June, the governor commuted the sentences of 57 inmates who were vulnerable to the virus. There have been 829 confirmed cases in prison system facilities, including staff members and inmates, according to the department’s records . Six people have died.
At the Oregon State Penitentiary, 36 staff members and 143 inmates have tested positive.
F.D.A. regulators defend their integrity and allude to potential interference.
The F.D.A. commissioner, Dr. Stephen Hahn, praised the statement on Thursday, saying that the authors “took the initiative to independently express their steadfast trust in the expertise and commitment of our organization.”Credit...Oliver Contreras for The New York Times
In an opinion column published in USA Today on Thursday, eight top regulators at the Food and Drug Administration promised to uphold the scientific integrity of their work and defend the agency’s independence. The column warned that “if the agency’s credibility is lost because of real or perceived interference, people will not rely on the agency’s safety warnings.”
The pledge by career scientists in the federal government came amid mounting concerns over the role the White House has played in emergency approvals for coronavirus therapies, including convalescent plasma and the malaria drug hydroxychloroquine, which the agency later revoked .
The specter of political arm-twisting has grown as several drugmakers entered large late-stage vaccine trials this summer. President Trump told reporters on Monday that “we’re going to have a vaccine very soon, maybe even before a very special date.”
That timeline, framed around Election Day, has been widely challenged by the administration’s top health officials, who have said that a vaccine approval by early November was improbable.
The statement in USA Today was written in large part because of fears over political influence on the F.D.A., including from the White House, according to senior administration officials familiar with the effort.
Prospects for any additional stimulus to address the pandemic’s devastating toll before the presidential election darkened considerably on Thursday, when a whittled-down Republican plan failed in the Senate on a partisan vote .
More than 150 business leaders in New York City sent a letter warning Mayor Bill de Blasio that he needed to take more decisive action to address crime and other quality-of-life issues that they said were jeopardizing the city’s economic recovery. Chief executives of companies like Goldman Sachs, Vornado Realty Trust and JetBlue signed the letter . Mr. de Blasio responded in a conciliatory tone, urging business leaders to work with him and arguing that the city needed federal funding and new borrowing capacity.
The U.S. commemorates Sept. 11 at another time of harrowing loss.
During the coronavirus pandemic, the United States has exceeded the death toll of Sept. 11, 2001, by many orders of magnitude.Credit...Brittainy Newman for The New York Times
The families, the politicians and the bagpipers gathered once more at ground zero on Friday, as the country paused to remember a national crisis even as it found itself in the midst of another .
The somber rituals held at the Sept. 11 memorial in Lower Manhattan provided an especially poignant resonance in the face of a pandemic that has crippled the country and brought particularly devastating loss to New York City.
And having already transformed so many rhythms of life, the outbreak also altered a collective moment to honor the dead.
Though the names of the victims resounded across the plaza, and the bells tolled across New York as they have in years past, there was no stage in front of those who came to mourn.
Some of America’s most notable politicians were in attendance, including Vice President Mike Pence and Joseph R. Biden Jr., the Democratic nominee for president, but all of them wore masks in addition to their customary memorial ribbons and lapel pins. They exchanged elbow bumps, then distanced themselves six feet apart as they stood for the national anthem.
It has been 19 years since passenger jets hijacked by terrorists slammed into the World Trade Center and the Pentagon and crashed into a field in Shanksville, Pa. Nearly 3,000 lives were lost, some 2,700 of them in New York, in the deadliest attack in the country’s history, a blow to America’s psyche.
Now, the United States confronts a far deadlier calamity. During the pandemic, the United States has exceeded the death toll of Sept. 11, 2001, by orders of magnitude . In New York City alone, more than 23,000 people have died of the virus .
In both tragedies, the eyes of the nation turned to New York, looking to see how a city brought to its knees would stagger back to recovery.
“It’s two of the most traumatic things that have ever happened to New York City, and it’s probably changed it forever,” said Diane Massaroli, whose husband, Michael, was killed in the World Trade Center.
Having transformed so many aspects of daily life, the pandemic thus affected one of the city’s most sacred and solemn moments. The family members gathered at the Sept. 11 memorial’s eight-acre site in Lower Manhattan were asked to stay socially distant, and others were discouraged from gathering near the spot known as ground zero.
French officials vow to cut down testing delays amid a spike in cases and hospitalizations.
A Covid-19 patient in a hospital in Marseille on Friday. France is seeing a worrisome uptick in cases and hospitalizations.Credit...Christophe Simon/Agence France-Presse — Getty Images
France is facing a worrying surge in cases, the government said on Friday, warning that the new cases were rapidly increasing and that hospitals were seeing an uptick in admissions.
But the authorities did not announce new rules, vowing instead to improve the country’s massive testing program — which has been plagued by delays in recent weeks — and urging the French to continue social distancing measures.
The country registered about 54,000 new cases over the past 7 days — less than Spain , but far more than other neighboring countries like Italy or Germany. Nearly 31,000 people in France have died of the virus.
On Thursday, there were nearly 10,000 new confirmed cases, a record since the beginning of the epidemic. The surge is due partly to widespread testing, but the positivity rate for those tests has also increased — it was at 5.4 percent this week, up from 1.5 in late July — meaning that the virus is picking up speed.
Jean Castex, the French prime minister, said in a televised address on Friday that authorities were particularly worried about a renewed increase in the number of hospitalizations, especially of elderly people.
“This shows there is no Maginot line,” said Mr. Castex, referring to national fortifications built in the 1930s. Even if the virus is still mostly spreading among younger people, he said, it “inevitably” ends up reaching more vulnerable segments of the population.
In other developments around the world:
Myanmar has locked down half of its largest city, Yangon, and halted travel between regions in an effort to halt the spread of the virus. Myanmar’s leader, Daw Aung San Suu Kyi, urged the public to follow health protocols in a nationally televised address on Thursday. The number of confirmed cases has gone up fivefold in less than three weeks, reaching 2,422 on Friday, with 14 deaths, according to a Times database .
India on Friday reported a record 96,551 new cases, pushing the country’s total caseload above 4.5 million, according to a New York Times database . More than 76,000 deaths have been linked to Covid-19.
The U.S. extradition hearing in London for Julian Assange, the WikiLeaks founder, will resume on Monday, Reuters reported. The hearing was postponed on Thursday over fears that a lawyer involved in the case may have come into contact with someone with the coronavirus, but the lawyer tested negative.
North Korea has deployed crack troops along its border with a shoot-to-kill order to prevent smugglers from introducing the coronavirus into its isolated and malnourished population, the United States’ top general in South Korea, Gen. Robert B. Abrams, said on Thursday. North Korea insists that it has not confirmed a single case of Covid-19. But outside experts are skeptical, citing the country’s decrepit public health capabilities and the long border it shares with China, where the epidemic first erupted.
New studies underscore the gravity of Britain’s surge.
Spectators watching The Royal Ballet perform beside the Regent's Canal in London on Aug. 30. The virus is surging again in Britain.Credit...Isabel Infantes/Agence France-Presse — Getty Images
A series of studies released on Friday offered the strongest evidence yet that the coronavirus is surging again in Britain, suggesting that the country may be following other European nations in seeing significant new spikes of the virus.
Scientists from Imperial College London said that the prevalence of coronavirus infections doubled every eight days from late August to early September in England, a significant quickening of the spread.
The scientists tested a random sample of 150,000 people and estimated that the so-called reproduction number — a measure of how many people on average a single patient will infect — was 1.7, indicating a growing outbreak. An R number below 1 would indicate a dwindling outbreak.
And the government’s Office for National Statistics estimated that around 3,200 people , not counting those in hospitals or nursing homes, became infected with the virus every day in England during the week starting Aug. 30.
The British government reported 3,539 new daily cases on Friday, lifting its seven-day average well over 2,500, a level last seen in May. Its total caseload has surpassed 361,000, with more than 41,600 deaths.
Heeding the surge, Prime Minister Boris Johnson announced this week that the government would ban gatherings of more than six people . But with students now returning to school and Britons socializing inside more as the weather cools, scientists said that might not be enough.
“This is a massive blow to the government’s strategy to contain the spread of Covid-19,” Simon Clarke, an associate professor at the University of Reading, said of the Imperial College London study.
Mr. Johnson has been encouraging people to go back to work, eat out at restaurants, patronize pubs and send children back to school. Many Britons have also remained resistant to wearing face masks in crowded places.
Britain’s new contact-tracing app will be introduced in England and Wales on Sept. 24, Mr. Johnson’s government announced on Friday. The government had previously been criticized over the long delay; earlier versions were scrapped months ago .
The app will allow people to scan QR codes when they visit hospitality venues and will use Apple and Google’s technology for detecting other smartphones in the vicinity to log location data necessary for contact tracing.
How can countries’ responses be compared? Think of the virus like a marathon.
What’s the fairest expectation of how bad the pandemic should have been in the United States?
In his Morning newsletter, David Leonhardt spoke with Donald McNeil, the New York Times reporter who has frequently appeared on “The Daily” podcast to talk about the coronavirus.
Donald makes a fascinating point: Don’t look only at snapshots, like a country’s per capita death toll. “It’s not fair to pick one point in time and say, ‘How are we doing?’” he writes. “You can only judge how well countries are doing when you add in the time factor” — that is, when the virus first exploded in a given place and what has happened since.
The pandemic, he adds, is like a marathon with staggered start times.
The virus began spreading widely in Europe earlier than in North America. Much of Europe failed to contain it at first and suffered terrible death tolls. The per capita toll in a few countries, like Britain, Italy and Spain, remains somewhat higher than in the U.S. But those countries managed to get the virus under control by the late spring. Their caseloads plummeted.
In the U.S., the virus erupted later — yet caseloads never plummeted. Almost every day for the past six months, at least 20,000 Americans have been diagnosed with the virus. “Europe learned the hard lesson and applied remedies,” as Donald says. “We did not, even though we had more warning.”
This chart makes the point:
Credit...By The New York Times | Sources: Johns Hopkins University and World Bank
The population-adjusted death toll in the U.S. surpassed Western Europe’s two months ago. The U.S. toll is far above those of France, Germany, Canada, Japan, Australia and many other countries — and is on pace to overtake Italy’s in the next few days and Britain’s and Spain’s not long after that.
Donald does add one important caveat. “We won’t really be able to judge until it’s over,” he says. Cases have recently begun rising again in Spain and some other parts of Europe , raising the possibility that Europe is on the verge of a new surge of deaths. In the U.S., Labor Day gatherings and the reopening of some schools may cause new outbreaks — or may not.
For now, the simplest summary seems to be this: Adjusting for time, there is no large, rich country that has suffered as much as the U.S.
Missed vaccines, skipped colonoscopies: Preventive care plummets in the U.S.
Last month in New York City, drug stores were already advertising flu shots, which health officials were urging people to get early. Demand for vaccines and other preventive care has declined sharply since the arrival of coronavirus.Credit...Bryan R. Smith/Agence France-Presse — Getty Images
When the pandemic hit, Americans vastly scaled back on preventive health, and there is little sign that this deferred care will be made up .
Vaccinations dropped by nearly 60 percent in April, and almost no one was getting a colonoscopy, according to new data from the nonprofit Health Care Cost Institute.
The data, drawn from millions of health insurance claims, shows a consistent pattern, whether it was prostate screenings or contraceptives: Preventive care declined drastically this spring and, as of late June, had not yet recovered to normal levels. Many types of such care were still down by a third at the start of this summer, the most recent data available shows, as Americans remained wary of visiting hospitals and medical offices.
Americans continued seeking care they couldn’t avoid — hospital admissions for childbirth, for example, held steady — but avoided care they could put off. More invasive preventive procedures, such as mammograms and colonoscopies, showed the greatest decline.
Colonoscopies, which are generally used to screen for colon cancer, declined by 88 percent in mid-April and were still 33 percent lower than normal at the end of June. Mammograms, which fell 77 percent at the height of the pandemic, are still down 23 percent.
Critical childhood vaccinations for hepatitis, measles, whooping cough and other diseases also declined significantly, a trend that had already begun to worry pediatricians earlier in the pandemic. Of particular concern, measles vaccinations fell 73 percent in mid-April and were still down 36 percent at the end of June.
But one preventive service stayed relatively steady through the pandemic: pregnancy-related ultrasounds. Those declined slightly in March and April but never fell more than 20 percent below 2019 levels. Insertions of IUDs, one of the most effective birth control methods, declined like other preventive care — raising the possibility of an increase in pregnancies in coming months.
Florida will reopen bars on Monday, and Puerto Ricans can go back to the beach.
An empty bar in St. Petersburg, Fla., that was closed in June when drinking at bars was banned as the state experienced a coronavirus surge.Credit...Eve Edelheit for The New York Times
Halsey Beshears, Florida’s secretary for the Department of Business and Professional Regulation, announced on Twitter on Thursday that the state would allow bars to operate at half capacity starting Monday. He rescinded an executive order from June that had banned drinking at bars as the state experienced a surge.
Gov. Ron DeSantis, a Republican, had hinted earlier on Thursday that his administration would not only soon allow the reopening of bars and restaurants but also forbid future closures.
“I think that we probably need to just have it that everyone knows they’ll be able to operate,” he said. “The closures are just totally off the table, because it’s hard to plan if you think you have the sword of Damocles hanging over your head.”
Bars, however, seem likely to remain closed in Miami-Dade, the state’s most populous county and where the virus has hit hardest. Mayor Carlos Gimenez said Wednesday that bars and nightclubs, which have been shut down by county order since March, would remain shuttered.
“The activities there are not conducive to maintaining a six-feet separation,” he said. “I don’t foresee us opening bars and nightclubs here for the foreseeable future — until we get a vaccine.”
In Puerto Rico, Gov. Wanda Vázquez eased some of the island’s tight restrictions on Thursday, citing a recent drop in cases. Ms. Vázquez lifted a lockdown that had forced people to stay home on Sundays, and reopened beaches to everyone. She also authorized the reopening of gyms, movie theaters and casinos at 25 percent capacity.
Bars and nightclubs remain closed, and a nightly curfew will remain in effect.
Reporting was contributed by Aurelien Breeden, Kenneth Chang, Choe Sang-Hun, Emily Cochrane, Abdi Latif Dahir, Marie Fazio, Emma G. Fitzsimmons, Michael Gold, Peter S. Goodman, Sophie Hardach, Sarah Kliff, David Leonhardt, Dan Levin, Patricia Mazzei, Benjamin Mueller, Saw Nang, Richard C. Paddock, Roni Caryn Rabin, Dana Rubinstein, Karan Deep Singh, Megan Specia, Jim Tankersley, Kate Taylor and Noah Weiland.
"""



doc = nlp( raw_text )
unique_words= {}

for token in doc:
    temp_int  = token._.syllables_count
    if( temp_int != None and token.lemma_ != '-PRON-' ):
        unique_words[token.lemma_] = token._.syllables_count
        


diff_words= {}
all_words=[]
freqs=[]
lens=[]
syl_count=[]

for lemma in unique_words:
    frq=zipf_frequency(lemma, 'en')
    all_words.append(lemma)
    freqs.append (frq)
    lens.append (len(lemma))
    syl_count.append(unique_words[lemma])


df=pd.DataFrame ()

df['words'] = all_words
df['freq'] = freqs
df['lens'] = lens
df['syl_count'] = syl_count

df['freq_z'] = -(df.freq - df.freq.mean())/df.freq.std(ddof=0)
df['lens_z'] = (df.lens - df.lens.mean())/df.lens.std(ddof=0)
df['syl_count_z'] = (df.syl_count - df.syl_count.mean())/df.syl_count.std(ddof=0)
df['tabulate']=df['freq_z']+0.8*df['lens_z']+0.3*df['syl_count_z']
df=df.sort_values('tabulate', ascending=False)


index=0
import json
with open("FlaskAPI/dictionary_compact.json") as f:
    webster = json.load(f)


for wd in df['words']:
    if (index<10):
        if( wd in webster ):
            print (wd)
            print ( webster[wd] )
            print()
            diff_words[wd] = webster[wd]
            index=index+1
    else:
        break
    
    
