import streamlit as st
from PIL import Image

# from st_pages import Page, show_pages
# show_pages(
#     [
#         # Page("main.py", "Home", "🏠"),
#         Page("molecule_examine.py", "Molecule Examine", "🧫"),
#         Page("chat.py", "ChatAI", "🪬"),
#         Page("about_us.py", "About us", "🧑🏻‍🔬")
#     ]
# )

image = Image.open('/Users/artemkhilalov/Studying/machine_learning/academic_internship_work/streamlit_project/logo-site.png')
st.image(image)

st.title('О нас')
st.write('В Johnson & Johnson мы верим, что хорошее здоровье - это основа яркой жизни, '
         'процветающих сообществ и поступательного прогресса. Вот почему вот уже более 135 лет мы стремимся к тому, '
         'чтобы люди были здоровы в любом возрасте и на каждом этапе жизни. Сегодня, являясь крупнейшей в мире и '
         'наиболее диверсифицированной компанией по производству медицинских товаров, мы стремимся использовать '
         'наш охват и размер во благо. Мы стремимся улучшить доступ и ценовую доступность, '
         'создать более здоровые сообщества и сделать здоровый дух, тело и окружающую среду доступными для всех и везде.')
st.write('Каждый день более 150 000 наших сотрудников по всему миру объединяют усилия сердца, '
         'науки и изобретательности, чтобы коренным образом изменить траекторию развития здравоохранения человечества.')
st.header('Наше наследие: более 135 лет заботы')
st.write('*Ценности, которыми мы руководствуемся при принятии решений, изложены в нашем кредо. Проще говоря, наше кредо призывает нас ставить на первое место потребности и благополучие людей, которым мы служим.*')
st.write('*Роберт Вуд Джонсон, бывший председатель правления с 1932 по 1963 год и член семьи основателей компании, сам сформулировал наше кредо в 1943 году, незадолго до того, как Johnson & Johnson стала публичной компанией. Это было задолго до того, как кто-либо услышал термин “корпоративная социальная ответственность”. Наше кредо - это нечто большее, чем просто моральный компас. Мы считаем, что это залог успеха в бизнесе. Доказательством этого является тот факт, что Johnson & Johnson - одна из немногих компаний, которые процветали на протяжении более чем столетия перемен.*')
st.subheader('Наше кредо')
st.write('Мы считаем, что наша главная ответственность лежит на пациентах, врачах и медсестрах, матерях и отцах и всех остальных, кто пользуется нашими продуктами и услугами. Для удовлетворения их потребностей все, что мы делаем, должно быть высокого качества. Мы должны постоянно стремиться обеспечивать ценность, снижать наши издержки и поддерживать разумные цены. Заказы клиентов должны выполняться быстро и точно. Наши деловые партнеры должны иметь возможность получать справедливую прибыль.')
st.write('Мы несем ответственность перед нашими сотрудниками, которые работают с нами по всему миру. Мы должны обеспечить инклюзивную рабочую среду, в которой каждый человек должен рассматриваться как личность. Мы должны уважать их разнообразие и достоинство и признавать их заслуги. У них должно быть чувство безопасности, самореализации и целеустремленности в своей работе. Компенсация должна быть справедливой и адекватной, а условия труда - чистыми, упорядоченными и безопасными. Мы должны поддерживать здоровье и благополучие наших сотрудников и помогать им выполнять свои семейные и другие личные обязанности. Сотрудники должны чувствовать себя свободными в высказывании предложений и жалоб. Для лиц, имеющих соответствующую квалификацию, должны быть созданы равные возможности для трудоустройства, развития и продвижения по службе. Мы должны обеспечить высококвалифицированных лидеров, и их действия должны быть справедливыми и этичными.')
st.write('Мы несем ответственность перед сообществами, в которых живем и работаем, а также перед мировым сообществом. Мы должны помогать людям быть здоровее, поддерживая улучшение доступа и ухода в большем количестве мест по всему миру. Мы должны быть добропорядочными гражданами — поддерживать добрые дела и благотворительность, улучшать здравоохранение и образование и платить свою справедливую долю налогов. Мы должны поддерживать в надлежащем порядке собственность, которой нам выпала честь пользоваться, защищая окружающую среду и природные ресурсы.')
st.write('Наша конечная ответственность лежит на наших')
