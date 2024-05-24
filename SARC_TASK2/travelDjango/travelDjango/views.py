from django.shortcuts import render

def home(request):
        
        name = request.POST.get('dropdown')
        print(name)

        if name == 'Kamakhya':
                place ='KAMAKHYA TEMPLE'
                about ="""
                Nestled amidst the Nilachal hills in Guwahati, Assam, lies the Kamakhya Temple, a sacred pilgrimage site pulsating with the power of Shakti, the divine feminine force in Hinduism. Renowned as one of the 51 Shakti Peethas, it is believed to mark the spot where the yoni (genitals) of Sati, the consort of Lord Shiva, fell after his cosmic dance with her corporeal form.

                The temple's origins are veiled in the mists of time, though ancient texts like the Kalika Purana and the Rudrayamala Tantra hint at its significance for centuries. The present structure, a captivating blend of architectural styles, dates back to the 16th century, built by King Naranarayan after a previous temple's destruction.

                The Kamakhya Temple complex is a captivating labyrinth of shrines, each radiating a unique energy. The focal point is the Garbhagriha, the main sanctum. Unlike conventional temples with idols, it's a natural cave housing a revered rock formation symbolizing the embodiment of the Goddess. This unique feature sets Kamakhya apart from other Hindu pilgrimage sites.

                The temple is intrinsically linked to the Ambubachi Mela, an annual celebration unlike any other. During this time, the temple remains closed for three days, mirroring the belief that the Goddess undergoes her menstrual cycle. This unique association with menstruation, a natural biological process often shrouded in stigma, highlights Kamakhya's celebration of feminine power in its entirety.

                Kamakhya Temple attracts devotees from across the spectrum of Hinduism. It is a focal point for Shakta Hindus, who worship the Goddess in her fierce and powerful aspects. Tantric practitioners also revere the temple for its association with esoteric practices and rituals. However, the temple welcomes all Hindu devotees seeking blessings, irrespective of their specific sect or belief system.

                Beyond its religious significance, Kamakhya Temple stands as a testament to Assam's rich cultural heritage. The intricate carvings adorning the temple walls depict stories from Hindu mythology, while the vibrant festivals showcase the state's unique traditions and customs. A visit to Kamakhya Temple is not just a spiritual journey; it's a portal to a world steeped in history, mythology, and the unwavering power of the divine feminine."""
        elif name == 'Navagraha':
                place = 'NAVAGRAHA TEMPLE'
                about ="""
        High atop the scenic Chitrasal hills, also known as Navagraha Hill, in Guwahati, Assam, rests the celestial gem – the Navagraha Temple. Unlike many grand Hindu temples, Navagraha doesn't enshrine a single deity, but instead honors the nine celestial bodies revered in Vedic astrology – the Navagrahas.

        Constructed in the late 18th century by the powerful Ahom king Rajeswar Singha, the temple has witnessed its share of history. Though partially damaged by an earthquake, it stands restored and continues to be a significant pilgrimage site. The ascent to the temple offers breathtaking panoramic views of Guwahati city and the mighty Brahmaputra River, adding to the spiritual and scenic experience.

        The temple's architectural style is relatively simple, with a focus on the symbolic representation of the Navagrahas. Inside the main sanctum lie nine Shivalingas – the iconic representation of Lord Shiva – each adorned with a distinct colored cloth. These colors correspond to the celestial bodies they symbolize: red for Mars, white for Venus, blue for Saturn, and so on. Devotees believe that offering prayers and performing specific rituals like puja (worship), homa (fire rituals), and shanti (peace invocations) for each planet can appease their influences and bring positive changes to their lives.

        Beyond its religious significance, the Navagraha Temple is also an intriguing hub for astronomical and astrological studies. The temple houses a library containing ancient manuscripts and books on these subjects, offering a glimpse into the rich history of these practices in India. Additionally, a telescope allows visitors to observe celestial bodies, fostering a connection between the physical and the divine.

        The Navagraha Temple attracts devotees from various backgrounds. Astrologers visit to seek guidance and inspiration, while those seeking remedies for perceived planetary imbalances in their lives come to perform specific pujas. General pilgrims visit to pay homage to the Navagrahas, believing that seeking their blessings can bring peace, prosperity, and good fortune.

        Standing tall amidst the verdant hills, the Navagraha Temple of Guwahati is a unique confluence of faith, astronomy, and astrology. It's a testament to the enduring belief system in India and offers a captivating experience for pilgrims, history buffs, and astronomy enthusiasts alike
        """
        else:
                place = 'BASISTHA TEMPLE'
                about = """
        Shrouded in the serenity of Guwahati's outskirts lies the Basistha Temple, a place where ancient legends intertwine with spiritual reverence. Dedicated to Lord Shiva, this temple complex is not just a pilgrimage site, but a gateway to the storied life of Sage Vasistha, believed to have established the ashram where the temple resides.

        The history of the Basistha Temple stretches back to the Vedic age. Legends claim Sage Vasistha, a revered figure in Hindu mythology, founded the ashram. The Kalika Purana even goes so far as to describe it as one of the seven Shakti Peethas. As the story goes, Vasistha, on his way to pay respects to Goddess Kamakhya, was obstructed by King Naraka. The enraged sage cursed the king and established his hermitage at the scenic Shandhyachal hills, where he is said to have meditated on Lord Shiva until his final days. His tomb lies within the temple complex, a testament to his spiritual journey.

        The temple itself, built by Ahom king Rajeswar Singha in the 18th century, reflects the architectural style of Assam. Constructed near the Basistha river, the complex offers a serene escape. Visitors are greeted by a red-hued temple in the typical Assamese style, perched at a higher level. Closer to the river, another temple adorned with Ganesha idols on its outer walls beckons attention.

        Beyond the visual beauty, the Basistha Temple complex holds a captivating charm. A short trek leads you to a hidden cave where Sage Vasistha is said to have meditated. The nearby Garbhanga Reserve Forest, teeming with elephants and a proposed butterfly haven, adds to the natural allure. The sound of cascading waterfalls and the vibrant wildlife create a symphony that complements the spiritual aura of the place.

        The Basistha Temple isn't just a destination for devotees of Lord Shiva. It's a place where history, mythology, and nature converge. Here, you can trace the footsteps of the revered Sage Vasistha, seek blessings at the ancient temple, and immerse yourself in the tranquility of the surrounding wilderness. It's a perfect blend of spiritual awakening and a rejuvenating escape for the soul"""

        data ={
                "place": place,
                "about":about
        }



        return render(request,'home.html',data)        

