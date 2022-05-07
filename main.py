import nltk
from wordcloud import WordCloud 
import matplotlib.pyplot as plt

korWa = """
The Korean War (also known by other names) was fought between North Korea and South Korea from 1950 to 1953. The war began on 25 June 1950 when North Korea invaded South Korea following clashes along the border and rebellions in South Korea. North Korea was supported by China and the Soviet Union while South Korea was supported by the United Nations, principally the United States. The fighting ended with an armistice on 27 July 1953.

In 1910, Imperial Japan annexed Korea, where it ruled for 35 years until its surrender at the end of World War II on 15 August 1945. The United States and the Soviet Union divided Korea along the 38th parallel into two zones of occupation. The Soviets administered the northern zone and the Americans administered the southern zone. In 1948, as a result of Cold War tensions, the occupation zones became two sovereign states. A socialist state, the Democratic People's Republic of Korea, was established in the north under the totalitarian communist leadership of Kim Il-sung while a capitalist state, the Republic of Korea, was established in the south under the authoritarian, autocratic leadership of Syngman Rhee. Both governments of the two new Korean states claimed to be the sole legitimate government of all of Korea, and neither accepted the border as permanent.

North Korean military (Korean People's Army, KPA) forces crossed the border and drove into South Korea on 25 June 1950. Joseph Stalin had final decision power and several times demanded North Korea postpone the invasion, until he and Mao Zedong both gave their final approval in spring 1950. The United Nations Security Council denounced the North Korean move as an invasion and authorized the formation of the United Nations Command and the dispatch of forces to Korea to repel it. The Soviet Union was boycotting the UN for recognizing Taiwan (Republic of China) as China, and China (People's Republic of China) on the mainland was not recognized by the UN, so neither could support their ally North Korea at the Security Council meeting. Twenty-one countries of the United Nations eventually contributed to the UN force, with the United States providing around 90% of the military personnel.

After the first two months of war, South Korean Army (ROKA) and American forces hastily dispatched to Korea were on the point of defeat, retreating to a small area behind a defensive line known as the Pusan Perimeter. In September 1950, a risky amphibious UN counteroffensive was launched at Incheon, cutting off KPA troops and supply lines in South Korea. Those who escaped envelopment and capture were forced back north. UN forces invaded North Korea in October 1950 and moved rapidly towards the Yalu River—the border with China—but on 19 October 1950, Chinese forces of the People's Volunteer Army (PVA) crossed the Yalu and entered the war. The UN retreated from North Korea after the First Phase Offensive and the Second Phase Offensive. Chinese forces were in South Korea by late December.

In these and subsequent battles, Seoul was captured four times, and communist forces were pushed back to positions around the 38th parallel, close to where the war had started. After this, the front stabilized, and the last two years were a war of attrition. The war in the air, however, was never a stalemate. North Korea was subject to a massive US bombing campaign. Jet-powered fighters confronted each other in air-to-air combat for the first time in history, and Soviet pilots covertly flew in defense of their communist allies.

The fighting ended on 27 July 1953 when the Korean Armistice Agreement was signed. The agreement created the Korean Demilitarized Zone (DMZ) to separate North and South Korea, and allowed the return of prisoners. However, no peace treaty was ever signed, and the two Koreas are technically still at war, engaged in a frozen conflict. In April 2018, the leaders of North and South Korea met at the DMZ and agreed to work toward a treaty to formally end the Korean War.

The Korean War was among the most destructive conflicts of the modern era, with approximately 3 million war fatalities and a larger proportional civilian death toll than World War II or the Vietnam War. It incurred the destruction of virtually all of Korea's major cities, thousands of massacres by both sides, including the mass killing of tens of thousands of suspected communists by the South Korean government, and the torture and starvation of prisoners of war by the North Koreans. North Korea became among the most heavily bombed countries in history. Additionally, several million North Koreans are estimated to have fled North Korea over the course of the war.
"""
korWa

stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend([',', '.', "´"])

words = [w.lower() for w in nltk.word_tokenize(korWa) if w not in stopwords and w.isalpha()]

cleaned_word = " ".join(words)
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
plt.figure(1,figsize=(13, 13))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()