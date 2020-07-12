# import pycurl
import httplib2
# from io import BytesIO
import re

# b_obj = BytesIO()
# crl = pycurl.Curl()

# URL list:
url_list = [('http://www.thehypertexts.com/The%20Best%20Long%20Poems%20of%20All%20Time.html','Long_Poem'),
            ('http://www.thehypertexts.com/Best%20Sonnets.htm','Sonnets'),
            ('http://www.thehypertexts.com/Best%20Villanelles.htm','Villanelles'),
            ('http://www.thehypertexts.com/Famous%20Ballads%20Best%20Ballads%20Timeline.htm','Ballads'),
            ('http://www.thehypertexts.com/Best%20Sestinas.htm','Sestinas'),
            ('http://www.thehypertexts.com/Best%20Rondels%20and%20Roundels.htm','Rondels'),
            ('http://www.thehypertexts.com/Best%20Kyrielles.htm','Kyrielles'),
            ('http://www.thehypertexts.com/Best%20Couplets%20of%20All%20Time.html','Couplets'),
            ('http://www.thehypertexts.com/Best%20Quatrains%20Ever.htm','Quatrains'),
            ('http://www.thehypertexts.com/Haiku%20Best%20Masters%20Translation%20.htm','Haiku'),
            ('http://www.thehypertexts.com/The%20Best%20Limericks%20of%20All%20Time.htm','Limeriks'),
            ('http://www.thehypertexts.com/Best%20Nonsense%20Verse.htm','Nosense'),
            ('http://www.thehypertexts.com/The%20Best%20Poems%20for%20Kids.htm','Kids'),
            ('http://www.thehypertexts.com/Best%20Humorous%20Poems%20Light%20Verse%20Funny%20Poems.htm','Humorous'),
            ('http://www.thehypertexts.com/Best%20Poem%20of%20All%20Time.htm','Best_Poem'),
            ('http://www.thehypertexts.com/Best%20Poems%20Ever%20Greatest%20Poetry%20of%20All%20Time.htm','Best_Poety'),
            ('http://www.thehypertexts.com/Masters_of_English_Poetry_and_Literature.html','Master'),
            ('http://www.thehypertexts.com/The%20Most%20Popular%20Poems%20of%20All%20Time.html','Popular'),
            ('http://www.thehypertexts.com/Best%20American%20Poetry%20of%20All%20Time.html','American'),
            ('http://www.thehypertexts.com/Best%20Poetry%20Translations.htm','Translation'),
            ('http://www.thehypertexts.com/The%20Best%20Anglo-Saxon%20Riddles%20and%20Kennings.htm','Anglo'),
            ('http://www.thehypertexts.com/Ancient%20Greek%20Epitaphs%20Epigrams%20Translations.htm','Ancient'),
            ('http://www.thehypertexts.com/English%20Poetic%20Roots%20Old%20English%20Poetry%20Scottish%20Poetry%20Irish%20Poetry%20Welsh%20Poetry.htm','English'),
            ('http://www.thehypertexts.com/Best%20Lyric%20Poetry.htm', 'Lyric'),
            ('http://www.thehypertexts.com/The%20Best%20Free%20Verse%20Poems%20of%20All%20Time.htm','Free'),
            ('http://www.thehypertexts.com/Best%20Story%20Poems.htm','Story'),
            ('http://www.thehypertexts.com/Epigrams_in_Literature_and_Poetry.htm', 'Epigram'),
            ('http://www.thehypertexts.com/The%20Most%20Beautiful%20Poems%20in%20the%20English%20Language.htm', 'Beautiful'),
            ('http://www.thehypertexts.com/The%20Most%20Beautiful%20Lines%20in%20the%20English%20Language.htm', 'Lines'),
            ('http://www.thehypertexts.com/The%20Most%20Beautiful%20Sonnets%20in%20the%20English%20Language.htm', 'Sonnets2'),
            ('http://www.thehypertexts.com/Best%20Elegies%20Dirges%20Laments%20and%20Poems%20of%20Mourning.html', 'Elegies'),
            ('http://www.thehypertexts.com/The%20Best%20Poems%20about%20Death%20and%20Loss.html', 'Death'),
            ('http://www.thehypertexts.com/Holocaust%20Poetry.htm', 'Holocaust'),
            ('http://www.thehypertexts.com/Hiroshima%20Poetry%20Prose%20and%20Art.htm','Hiroshima'),
            ('http://www.thehypertexts.com/Best%20Christian%20Poetry%20Best%20Religious%20Poetry%20Best%20Spiritual%20Poetry.htm', 'Religious'),
            ('http://www.thehypertexts.com/Heresy%20Hearsay%20Poetry%20Vulgar%20Blasphemous.htm', 'Heresey'),
            ('http://www.thehypertexts.com/Best%20Thanksgiving%20Poems%20and%20Poems%20of%20Gratitude.htm', 'Thanks'),
            ('http://www.thehypertexts.com/Best%20Autumn%20Poems%20Fall%20Poetry.htm', 'Autumn'),
            ('http://www.thehypertexts.com/Fall%20Poetry%20Autumn%20Poems.html', 'Fall'),
            ('http://www.thehypertexts.com/The%20Best%20Sad%20Poems%20Dark%20Poetry.htm', 'Dark'),
            ('http://www.thehypertexts.com/Halloween%20Poetry.htm', 'Hallowen'),
            ('http://www.thehypertexts.com/Best%20Supernatural%20Poetry.htm', 'Supernatural'),
            ('http://www.thehypertexts.com/Best%20Christmas%20Poems.htm', 'Christimas'),
            ('http://www.thehypertexts.com/Best%20Vampire%20Poetry.htm', 'Vampire'),
            ('http://www.thehypertexts.com/Best%20Love%20Poems.htm', 'Love'),
            ('http://www.thehypertexts.com/Best%20Urdu%20Love%20Poetry%20English%20Translations.htm', 'Urdu'),
            ('http://www.thehypertexts.com/The%20Best%20Erotic%20Poems.html', 'Erotic'),
            ('http://www.thehypertexts.com/Best%20Romantic%20Poetry.htm', 'Romantic'),
            ('http://www.thehypertexts.com/Best%20Juvenilia%20by%20Poets%20Early%20Poems.htm', 'Juvenilia'),
            ('http://www.thehypertexts.com/The%20Ten%20Greatest%20Poems%20Ever%20Written.htm', 'Greatest'),
            ('http://www.thehypertexts.com/What%20is%20Poetry%20Definition%20Examples%20Analysis.html', 'Definition'),
            ('http://www.thehypertexts.com/Best%20Abstract%20Poetry.html', 'Abstract'),
            ('http://www.thehypertexts.com/Human%20Perfection.htm', 'Perfection'),
            ('http://www.thehypertexts.com/The%20Best%20Writing%20in%20the%20English%20Language.htm', 'English2'),
            ('http://www.thehypertexts.com/Best%20Poems%20about%20Mothers.htm', 'Mother'),
            ('http://www.thehypertexts.com/Poetry%20by%20Michael%20R.%20Burch.htm', 'Michael'),
            ('http://www.thehypertexts.com/The%20Best%20Medieval%20Poems%20in%20Modern%20English%20Translations.htm', 'Medieval'),
            ('http://www.thehypertexts.com/Epigrams_in_Literature_and_Poetry.htm', 'Epigrams'),
            ('http://www.thehypertexts.com/Best%20Easter%20Poems.htm', 'Easter'),
            ('http://www.thehypertexts.com/Consoling%20Poems%20the%20Best%20Poems%20of%20Consolation.htm', 'Consoling'),
            ('http://www.thehypertexts.com/Digby%20Dolben%20Best%20Poems%20Poet%20Poetry%20Picture%20Bio.htm', 'Digby'),
            ('http://www.thehypertexts.com/Best%20Princess%20Diana%20Poems.htm', 'Diana'),
            ('http://www.thehypertexts.com/Best%20Carpe%20Diem%20Poems.htm', 'Carpe'),
            ('http://www.thehypertexts.com/Best%20Didactic%20Poems.htm', 'Didatic'),
            ('http://www.thehypertexts.com/William%20Blake%20Best%20Poems.htm', 'William'),
            ('http://www.thehypertexts.com/Donald%20Trump%20Poetry%20the%20Best%20Poems%20of%20Donald%20Trump.htm', 'Donald'),
            ('http://www.thehypertexts.com/Gaza%20Poetry%20Poems%20for%20Gaza%20Nakba%20Palestinians.htm', 'Gaza'),
            ('http://www.thehypertexts.com/Albert%20Einstein%20Poet%20Poetry%20Poems%20Pictures%20Bio.htm', 'Eisten'),
            ('http://www.thehypertexts.com/Haiti%20Poems%20and%20Poetry%20for%20Haitian%20Earthquake%20Victims.htm', 'Haiti'),
            ('http://www.thehypertexts.com/Marilyn%20Monroe%20Poet%20Poetry%20Picture%20Bio.htm', 'Monroe'),
            ('http://www.thehypertexts.com/Pope%20Poems%20Poetry%20By%20and%20About.htm', 'Pope'),
            ('http://www.thehypertexts.com/Rachel%20Joy%20Scott%20Poetry%20Quotations%20Art.htm', 'Rachel'),
            ('http://www.thehypertexts.com/Famous%20Drinking%20Songs%20Famous%20Drinking%20Poems.htm', 'Drinking'),
            ('http://www.thehypertexts.com/Best%20Poems%20of%20Modernism.html', 'Modernism'),
            ('http://www.thehypertexts.com/For%20Darfur%20Poets%20Poetry%20Literature%20Art%20Genocide.htm', 'Darfur'),
            ('http://www.thehypertexts.com/Arthurian%20Poems.htm', 'Arturian'),
            ('http://www.thehypertexts.com/Pope%20Francis%20Poems.htm', 'Francis'),
            ('http://www.thehypertexts.com/Sandy%20Hook%20Poems.htm', 'Sandy'),
            ('http://www.thehypertexts.com/Best%20Fathers%20Day%20Poems.html', 'Father'),
            ('http://www.thehypertexts.com/Robert%20Burns%20Translations%20Modern%20English.htm', 'Robert'),
            ('http://www.thehypertexts.com/Best%20Memorial%20Day%20Poems.htm', 'Memorial'),
            ('http://www.thehypertexts.com/Simon_Perchik_Poet_Poetry_Picture_Bio.htm', 'Simon'),
            ('http://www.thehypertexts.com/Bronislawa%20Wajs%20Papusza%20Poet%20Poetry%20Bio%20Picture%20Gypsy%20Poet%20Romani%20Poetry.htm', 'Bronislawa'),
            ('http://www.thehypertexts.com/Holocaust%20Poems%20for%20Students%20and%20Teachers.htm', 'Holocaust2'),
            ('http://www.thehypertexts.com/The%20Best%20Sentimental%20Poetry%20Good%20Bad%20Naive%20Life%20Death.html', 'Sentimental'),
            ('http://www.thehypertexts.com/Parkland%20Poems%20Marjory%20Stoneman%20Douglas%20High%20School.htm','Parkland'),
            ('http://www.thehypertexts.com/Michael%20R.%20Burch%20Erotic%20Poems.html', 'Michael2'),
            ('http://www.thehypertexts.com/Genocide%20Poetry.htm', 'Genocide'),
            ('http://www.thehypertexts.com/Janusz_Korczak_Poetry_Poems_Translations_%20by_Esther_Cameron.htm', 'Janusz'),
            ('http://www.thehypertexts.com/Aurora%20Poetry.htm', 'Aurora'),
            ('http://www.thehypertexts.com/Essays%20Articles%20Reviews%20Prose/Rejected%20Again%20the%20Bias%20Against%20Formal%20Metrical%20Rhyming%20Poems.htm', 'Essay'),
            ('http://www.thehypertexts.com/Best%20Celebrity%20Poems%20Epigrams%20Quotes%20Tweets.htm', 'Celebrity'),
            ('http://www.thehypertexts.com/Best%20Animal%20Poems.htm', 'Animal'),
            ('http://www.thehypertexts.com/Fadwa%20Tuqan%20Palestinian%20Poet%20Poetry%20Picture%20Bio.htm', 'Fadwa'),
            ('http://www.thehypertexts.com/The%20Best%20of%20The%20HyperTexts.htm', 'Hyper'),
            ('http://www.thehypertexts.com/Current_and_Back_Issues.htm', 'Issues'),
            ]

# Cleaning the HTML using regular expression
def cleanhtml(raw_html):
  # cleanr = re.compile('<.*?>')
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

n_words = 0

for url, name in url_list:

    h = httplib2.Http(".cache")
    (resp_headers, content) = h.request(url, "GET")
    clean_text = cleanhtml(str(content))

    with open("html_data/"+name+".txt", "w") as output:
        output.write(clean_text)


# SCIPT using pycurl:

# for url, name in url_list:
#
#     b_obj = BytesIO()
#     crl = pycurl.Curl()
#
#     # Set URL value
#     crl.setopt(crl.URL, url)
#
#     # Write bytes that are utf-8 encoded
#     crl.setopt(crl.WRITEDATA, b_obj)
#
#     # Perform a file transfer
#     crl.perform()
#
#     # End curl session
#     crl.close()
#
#     # Get the content stored in the BytesIO object (in byte characters)
#     get_body = b_obj.getvalue()
#
#     print('Output of GET request:\n%s' % get_body.decode('utf8'))
#     # word_list = str.split(cleanhtml(get_body))
#     # word_list = cleanhtml(word_decoded)
#
#     # word_decoded = word_list.decode('utf8')
#     # n_words += len(word_list)
#     # print(str(word_list))
#
#     # with open("html_data/"+name+".txt", "w") as output:
#     #     output.write(str(word_list))
