from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from AI import AI


def english_nums(text):
    text = text.replace("١", "1")
    text = text.replace("۱", "1")
    text = text.replace("٢", "2")
    text = text.replace("۲", "2")
    text = text.replace("٣", "3")
    text = text.replace("۳", "3")
    text = text.replace("٤", "4")
    text = text.replace("۵", "5")
    text = text.replace("٥", "5")
    text = text.replace("٦", "6")
    text = text.replace("٧", "7")
    text = text.replace("٨", "8")
    text = text.replace("٩", "9")
    text = text.replace("۹", "9")
    text = text.replace("٠", "0")
    text = text.replace("۰", "0")
    text = text.replace(".", ".")
    return text


class Loader:
    def __init__(self, file_name):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0, length_function=len,
                                                       # separators=["\\(۵", "۵\\(", "\\(۱", "۱\\("],
                                                       separators=["\\d\\.", "\\.\\d"],
                                                       is_separator_regex=True)
        self.all_texts = []
        self.ai = AI()
        self.file_path = "Data/Problems/{name}.pdf"
        self.file_name = file_name
        self.loader = PyPDFLoader(self.file_path.format(name=self.file_name))
        self.pages = self.loader.load()

    def do_translation(self):
        f = open("Translation/{name}.tex".format(name=self.file_name), "w")
        for i in range(0, len(self.all_texts)):
            text = self.ai.translate(self.all_texts[i]),
            print(text, file=f)
            print(text)
            print("\\\\", file=f)

    def load_and_split(self):
        pass


class Loader1(Loader):

    def load_and_split(self):
        i = 0
        for page in self.pages[1:]:
            content = page.page_content
            split_text = self.splitter.split_text(content)
            for s in split_text[1:]:
                self.all_texts.append(s)
                print(s)
                print("-----------------------------------------" + str(i))
                i += 1


class Loader1390(Loader):
    def load_and_split(self):
        for page in self.pages:
            content = page.page_content
            split_text = self.splitter.split_text(content)
            for s in split_text[1:]:
                self.all_texts.append(s)
                print(s)
                print("-----------------------------------------")
        self.all_texts[8] += self.all_texts[9]
        self.all_texts.pop(9)
        print(self.all_texts[8], self.all_texts[9])


class Loader1392(Loader):
    def load_and_split(self):
        i = 0
        for page in self.pages:
            content = page.page_content
            split_text = self.splitter.split_text(content)
            for s in split_text:
                self.all_texts.append(s)
        self.all_texts[0] = """های رياضيات، ادبيات و فيزيک سه سال دبيرستان ( ۹ 􀀁 کردن کتاب 􀀁 خواهد برای دوره 􀀁 ۱. سينا می
ها مطالعه شود (برای 􀀁 های هر مبحث به ترتيب پاية آن 􀀁 نحوی که کتاب 􀀁 ريزی کند به 􀀁 کتاب) برنامه
تواند 􀀁 مثال کتاب فيزيک ۱ پيشاز کتاب فيزيک ۲ مطالعه شود). او به چند ترتيب مختلف می
ها را مطالعه کند؟ 􀀁 همة کتاب"""
        self.all_texts[1] = """قدر است؟ 􀀁 چه x۶ + y . مقدار ۶ x۲ + y۲ = و ۴۰ x + y = دو عدد حقيقی هستند که ۶ y و x"""
        self.all_texts[2] = """BC و AD های اضلاع 􀀁 به ترتيب وسط N و M رو 􀀁 در شکل روبه
هستند. مساحت مستطيل چه مضربی از ABCD از مستطيل
چهارضلعی هاشورخورده است؟"""
        self.all_texts[3] = """به شکل رو به رو f : R ! R فرض کنيد نمودار تابع
شبيه کدام يک f(x)
x 􀀀 باشد. در اين صورت نمودار تابع ۱
ها در نقطة 􀀁 های زير است؟ (نمودارهای همة گزينه 􀀁 از گزينه
تعريف نشده هستند.) x = ۱"""
        self.all_texts[4] = """عليه مثبت داشته باشد و برابر 􀀁 ناميم، هرگاه حداقل سه مقسوم 􀀁 ۵. يک عدد طبيعی را کوچولو می
عليه مثبتش باشد. چند عدد کوچولو وجود دارد؟ 􀀁 ترين سه مقسوم 􀀁 مجموع کوچک"""
        self.all_texts[5] = """و CdAD ، BdAD های 􀀁 ای قرار گرفته که زاويه 􀀁 به گونه BC روی ضلع D نقطة ABC ۶. در مثلث
AB به ترتيب برابر ۱ و ۲ است. طول DC و BD های 􀀁 خط 􀀁 با هم برابرند و طول پاره AdBC
p قدر است؟ 􀀁 چ"""
        self.all_texts[6] = """از اعداد طبيعی به صورت زير تعريف شده است: a۰; a۱; a۲; : : : ۷. دنبالة 8<
:
a۰ = ۱;
an+۱ = ۱۳an (n  ۰):
چه عددی است؟ a رقم يکان ۱۳۹۲"""
        self.all_texts[7] = """در مورد اعداد زير کدام گزينه درست است؟
a = ۱۰۰!; b = ۲۱۰۰; c = ۲۲۲۲۲"""
        self.all_texts[8] = """واهيم با سه رنگ آبی، قرمز و سبز، هفت ناحية درون شکل 􀀁 می
های همسايه 􀀁 آميزی کنيم، به طوری که ناحيه 􀀁 رو را رنگ 􀀁 به 􀀁 رو
هايی که فقط در يک نقطه 􀀁 باشند (ناحيه 􀀁 های متفاوتی داشته 􀀁 رنگ
اشتراک دارند همسايه نيستند). اين کار به چند طريق ممکن
است؟"""
        self.all_texts[9] = """۲۱۹ متر بين زاهدان و مشهد احداث کرده = ۵۲۴; ۱۰ . وزارت راه و ترابری آزادراهی به طول ۲۸۸
های روشنايی کند. در 􀀁􀀁 است و قصد دارد در يک پروژة بلندمدت اين آزادراه را مجهز به چراغ
ترين قطعه 􀀁 راه که هيچ چراغی در آن نيست، نزديک 􀀁 هايی از آزاد 􀀁 ترين قطعه 􀀁 هر روز از بين بزرگ
شود. هزار و يکمين چراغی که 􀀁 به زاهدان انتخاب شده و در نقطة وسط آن يک چراغ نصب می
شود، چند متر با مشهد فاصله دارد؟ 􀀁 نصب می"""
        self.all_texts[10] = """گر با قابليتنمايشاعداد خيلی بزرگ 􀀁 حساب))، ماشينی استکه از يکصفحة نمايش 􀀁 ۱۱ . ((ضربين
حساب 􀀁 ، ضربين 􀀁 های ۱ الی ۹ تشکيل شده است. با فشار دادن هر دکمه 􀀁 هايی با شماره 􀀁 و دکمه
کند و حاصل را به 􀀁 گر را در عدد مربوط به آن دکمه ضرب می 􀀁 بلافاصله عدد صفحة نمايش
گر نوشته شده 􀀁 دهد. اگر ابتدا عدد ۱ روی صفحة نمايش 􀀁 نمايش می 􀀁 جای عدد قبلی در صفحه
های 􀀁 کم چند بار بايد از دکمه 􀀁 ۲۲۰۱۴ دست  ۳۱۴۳۵  باشد، برای به دست آوردن عدد ۵۱۳۹۲
حساب 􀀁 های ضربين 􀀁 توان با سه بار استفاده از دکمه 􀀁 حساب استفاده کرد؟ (برای مثال می 􀀁 ضربين
(.۷۲۹ = ۹  ۹  به ۷۲۹ دست يافت، زيرا ۹"""
        self.all_texts[11] = """توان يک مکعب ساخت؟ 􀀁 ها می 􀀁 چين 􀀁 های زير از روی خط 􀀁 ۱۲ . با تا کردن چند تا از شکل"""
        self.all_texts[12] = """کيفيت آزمون مرحلة اول سال گذشته به www:mathysc:ir گاه المپياد رياضی ايران ( 􀀁 ۱۳ . در وب
اند از ((خيلی خوب بود.))، ((عالی 􀀁 های نظرسنجی عبارت 􀀁 است. گزينه 􀀁 نظرسنجی گذاشته شده
گاه ثبت کند، درصد 􀀁 شد.))! پيشاز اين که عباسنظر خود را در وب 􀀁 تر از اين نمی 􀀁 بود.)) و ((به
، ها به ترتيب برابر ۵۰ ،۲۵ و ۲۵ بوده است. پس از ثبت نظر او اين نسبت به ۲۴ 􀀁 اين گزينه
قدر بوده است؟ 􀀁 کند. تعداد نظرهای ثبت شده پيش از ثبت نظر عباس چه 􀀁 ۴۸ و ۲۸ تغيير می
ها دقيق هستند.) 􀀁 (درصد"""
        self.all_texts[13] = """.p۲􀀀pq+q۲ = ها داشته باشيم ۳۷۲ 􀀁 از اعداد اول وجود دارد که برای آن (p; q) ۱۴ . چند زوج مرتب"""
        self.all_texts[14] = """ليه مثبت است، چند عامل اول دارد؟ 􀀁 ترين عدد طبيعی که دارای ۱۳۹۲ مقسوم 􀀁 ۱۵ . کوچک"""
        self.all_texts[15] = """چوپانی گوسفند گرسنة خود را در چراگاهی سرسبز با سه طناب مختلف به سه درخت بسته
خورد. 􀀁 رسی دارد را می 􀀁 هايی از چراگاه که به آن دست 􀀁 های همة قسمت 􀀁 است. گوسفند علف
تواند باشد؟ 􀀁 است، کدام شکل نمی 􀀁 های آن را خورده 􀀁 ای از چراگاه که گوسفند علف 􀀁 ناحيه"""
        self.all_texts[16] = """در يک پادگان ۱۱۹۶ سرباز در ۱۳ رديف ۹۲ تايی به شکل منظم
بيند اگر روی 􀀁 اند. آخرين سرباز از رديف آخر يکسرباز را می 􀀁 ايستاده
ها، سرباز ديگری نباشد. او چند سرباز از رديف 􀀁 خط واصل بين آن
کنيم.) 􀀁 بيند؟ (سربازها را نقطه فرض می 􀀁 اول را"""
        self.all_texts[17] = """رو خطوطی موازی اضلاع مثلث 􀀁 مطابق شکل روبه
ايجاد شود، A ′B ′C ايم تا مثلث ′ 􀀁 رسم کرده ABC
باشد. ABC ای که محيطش نصف محيط 􀀁 به گونه
است؟ AD چند برابر طول AB طول"""
        self.all_texts[18] = """y و x ها اعداد حقيقی 􀀁 گيريم که برای آن 􀀁 می a را مجموعة همة اعداد حقيقی مثل S ۱۹ . مجموعة
ای که 􀀁 موجود باشند، به گونه
a(a 􀀀 ۱) + x(x 􀀀 ۱) + y(y 􀀀 ۱) = ۳
۲
قدر است؟ 􀀁 است. طول اين بازه چه 􀀁 يک بازه S دانيم که 􀀁 م"""
        self.all_texts[19] = """های زير است. 􀀁 ۲۰ . تصوير عمود يک چهارضلعی مسطح در فضا روی سه صفحة مختصات به شکل
قدر است؟ 􀀁 های طول قطرهای اين چهارضلعی چه 􀀁 مجموع مرب"""
        self.all_texts[20] = """شود که در معادلات زير صدق کند؟ 􀀁 از اعداد حقيقی يافت می (x; y; z; t) ۲۱ . چند چهارتايی مرتب 8>>>>>><
>>>>>>:
xy + yz + zx = t۲
yz + zt + ty = x۲
zt + tx + xz = y۲
tx + xy + yt = z۲"""
        self.all_texts[21] = """وزارت نفت کانالی بين بوشهر و ايلام حفر کرده است و قصد
دارد لولة انتقال گازی را در آن قرار دهد. سطح مقطع کانال
به شکل قسمتی از يک سهمی و سطح مقطع لوله به شکل
ای􀀁 يک دايره است. (منظور از سهمی نمودار يک چندجمله
درجه دوم است.) اگر عرض کانال برابر ۲ متر و عمق آن
توان در کانال 􀀁 ای که می 􀀁 ترين لوله 􀀁 ۴ متر باشد، شعاع بزرگ
ترين نقطة کانال تماس داشته 􀀁 قرار داد به طوری که با پايين
ها در شکل صحيح 􀀁 متر است؟ (نسبت اندازه 􀀁 باشد، چند سانتی
نيست.)"""
        self.all_texts[22] = """های 􀀁 است. خطی که وسط
p
به ترتيب ۲ و ۴ و ۷ ABC از مثلث BC و AC ،AB ۲۳ . طول اضلاع
شود در نقطة 􀀁 رسم می A ساز 􀀁 موازی با نيم B کند با خطی که از 􀀁 را به هم وصل می AC و AB
قدر است؟ 􀀁 چه AD کند. طول 􀀁 برخورد می D"""
        self.all_texts[23] = """پهلوان پوريای ولی از ياور خواسته که ۹ ميل زورخانه را از نقاطی که با دايرة توخالی نمايش
نحوی که مجموع فواصل ۹ جفت 􀀁 داده شده به نقاطی که با دايرة توپر نمايشداده شده ببرد، به
ترين مقدار ممکن شود. (دقت کنيد که در هر نقطه يک ميل 􀀁 نقطة ابتدايی و انتهايی، بيش
ترتيب بايد به کدام نقاط منتقل شوند؟ 􀀁 های الف و ب و ج به 􀀁 گيرد.) در اين صورت ميل 􀀁􀀁 قرار"""
        self.all_texts[24] = """تنها دزد شکرستان از دو سال پيش تحت تعقيب نظمية شکرستان قرار دارد. طبق تحقيقات
است، (برای مثال 􀀁 های او بين شکرستان و ۴ شهر همسايه به صورت زير بوده 􀀁 نظميه، تعداد سفر
است). اکنون او در کدام شهر مخفی 􀀁 اين دزد سه سفر از نمکستان شرقی به شکرستان داشته
است؟ 􀀁 شده
۱"""
        for s in self.all_texts[:25]:
            print(s)
            print("-----------------------------------------" + str(i))
            i += 1
        self.all_texts = self.all_texts[:25]


class Loader1394(Loader):

    def load_and_split(self):
        self.all_texts = [
                """1.ﺑﻪ ﭼﻨﺪ ﻃﺮﻳﻖ ﻣﯽﺗﻮﺍﻥ ﺍﻋﺪﺍﺩ۱،۲ﻭ ...،۶ﺭﺍ ﺩﺭ ﻳﮏ ﺭﺩﻳﻒﻧﻮﺷﺖﺑﻪﻃﻮﺭﯼ ﮐﻪ ﺍﺯ ﺑﻴﻦ ﻫﺮ ﺩﻭ ﻋﺪﺩ
ﻣﺠﺎﻭﺭ ﻳﮑﯽ ﺑﺮ ﺩﻳﮕﺮﯼ ﺑﺨﺶﭘﺬﻳﺮ ﺑﺎﺷﺪ؟
۱(۲٢(٤٣(٦٤(٨٥(١٠""",
                """.ﻣﺜﻠﺚ ﻗﺎﺋﻢﺍﻟﺰﺍﻭﻳﻪABCﺑﺎ ﻓﺮﺽ90BAC  
ﺭﺍﺩﺭ ﻧﻈﺮ ﺑﮕﻴﺮﻳﺪ. ﺩﺍﻳﺮﻩﺍﯼﺑﻪ ﻣﺮﮐﺰA
ﻃﻮﺭﯼ ﺭﺳﻢ ﻣﯽﮐﻨﻴﻢ ﮐﻪ ﺿﻠﻊABﺭﺍ ﺩﺭD،ﺿﻠﻊACﺭﺍ ﺩﺭFﻭﺿﻠﻊBCﺭﺍ ﺩﺭ ﺩﻭﻧﻘﻄﺔ
EﻭMﻗﻄﻊ ﮐﻨﺪ ﮐﻪ ﻧﻘﻄﺔEﺑﻴﻦ ﻧﻘﺎﻁDﻭMﺍﺳﺖ.ﻣﯽﺩﺍﻧﻴﻢMﻭﺳﻂ ﺿﻠﻊBCﺍﺳﺖ
ﻭﻫﻢﭼﻨﻴﻦﻧﺴﺒﺖﻃﻮﻝﮐﻤﺎﻥﻫﺎﯼDEﺑﻪEMﺑﻪMFﺑﺮﺍﺑﺮ ﺑﺎ ﻧﺴﺒﺖ۳ﺑﻪ۲ﺑﻪ۴ﺍﺳﺖ. ﻣﻘﺪﺍﺭ
ﻗﺪﺭﻣﻄﻠﻖ ﺗﻘﺎﺿﻞ ﺩﻭ ﺯﺍﻭﻳﺔﺣﺎﺩﺓﻣﺜﻠﺚABCﭼﻪﻗﺪﺭﺍﺳﺖ؟
۱(70
٢(50
٣(45
٤(30
٥(10""",
""".ﺟﻨﺎﺏﺧﺎﻥ ﻣﯽﺧﻮﺍﻫﺪﺑﺮﺍﯼﮔﺎﻭﺻﻨﺪﻭﻕ ﺧﻮﺩﺭﻣﺰ ﺍﻧﺘﺨﺎﺏ ﮐﻨﺪ ﻭ ﻫﺮ ﻫﻔﺘﻪ ﺭﻣﺰ
ﺁﻥ ﺭﺍ ﺗﻐﻴﻴﺮ ﺩﻫﺪ!ﺭﻣﺰ ﮔﺎﻭﺻﻨﺪﻭﻕ ﻳﮏ ﻋﺪﺩ ﺳﻪﺭﻗﻤﯽ ﺍﺳﺖ ﻭ ﺟﻨﺎﺏﺧﺎﻥ ﻣﺎﻳﻞ
ﺍﺳﺖﺍﺭﻗﺎﻡ ﺭﻣﺰ ﻣﺘﻤﺎﻳﺰﺑﺎﺷﻨﺪ ﻭ ﺑﻪﻋﻼﻭﻩ ﺍﺭﻗﺎﻡ ﺭﻣﺰ ﺟﺪﻳﺪ، ﺍﺯ ﺍﺭﻗﺎﻡ ﻣﺘﻨﺎﻇﺮ ﺩﺭ ﺭﻣﺰ
ﻗﺒﻠﯽﮐﻢﺗﺮﻧﺒﺎﺷﺪ.ﻣﺜﻼﹰ ﺍﮔﺮ ﻳﮏ ﺑﺎﺭ۲۵۹ﺭﺍ ﺍﻧﺘﺨﺎﺏ ﮐﺮﺩﺭﻣﺰ ﺑﻌﺪﯼ ﻧﺒﺎﻳﺪ۱۵۹
ﺑﺎﺷﺪ. ﺍﮔﺮ ﺍﻭﻟﻴﻦ ﺭﻣﺰ ﮔﺎﻭﺻﻨﺪﻭﻕ140ﺑﺎﺷﺪ، ﺍﻭ ﺣﺪﺍﮐﺜﺮﺑﻌﺪ ﺍﺯﭼﻨﺪﻫﻔﺘﻪﺩﻳﮕﺮ ﻧﻤﯽﺗﻮﺍﻧﺪ ﺑﻪ ﺍﻳﻦ ﺷﮑﻞ
ﺭﻣﺰ ﮔﺎﻭﺻﻨﺪﻭﻗﺶﺭﺍ ﺗﻐﻴﻴﺮ ﺩﻫﺪ؟)ﺗﻮﺟﻪ ﮐﻨﻴﺪﮐﻪ ﻫﻔﺘﺔ ﺍﻭﻝ،ﺭﻣﺰ ﻫﻤﺎﻥ۱۴۰ﺧﻮﺍﻫﺪ ﺑﻮﺩ.(
۱(۲۸٢(٢٤٣(٢٠٤(١٩٥(١٦""",
""".ﺗﺎﺑﻊ:f  ﻣﻔﺮﻭﺽ ﺍﺳﺖ. ﺑﺮﺍﯼ ﻫﺮm  ﻭn  ﺑﺎ ﺷﺮﻁ1( , )m n :
( )
m m
f n n
  1
ﮐﻪ ﻣﻨﻈﻮﺭ ﺍﺯ( , )m nﺑﺰﺭﮒﺗﺮﻳﻦ ﻣﻘﺴﻮﻡ ﻋﻠﻴﻪ ﻣﺸﺘﺮﮎmﻭnﺍﺳﺖ.ﮐﺪﺍﻡﻳﮏ ﺍﺯ ﮔﺰﺍﺭﻩﻫﺎﯼ ﺯﻳﺮ
ﺩﺭﺑﺎﺭﺓﺗﺎﺑﻊfﺩﺭﺳﺖ ﺍﺳﺖ؟
۱(ﺗﺎﺑﻊfﻳﮏﺑﻪﻳﮏ ﺍﺳﺖ.۲(ﺗﺎﺑﻊfﻳﮏﻧﻮﺍ )ﺻﻌﻮﺩﯼ ﻳﺎ ﻧﺰﻭﻟﯽ( ﺍﺳﺖ.
۳(ﺑﺮﺩ ﺗﺎﺑﻊfﺗﻤﺎﻡ ﺍﻋﺪﺍﺩ ﮔﻮﻳﺎ ﺍﺳﺖ.۴(ﺑﻪ ﺍﺯﺍﯼ ﻫﺮx  ﺩﺍﺭﻳﻢ( )f x x.
۵(ﻫﻤﺔﮔﺰﻳﻨﻪﻫﺎ ﺻﺤﻴﺢﻫﺴﺘﻨﺪ.
1""",
""".ﭼﻨﺪﻋﺪﺩ ﺳﻪ ﺭﻗﻤﯽabcﻭﺟﻮﺩ ﺩﺍﺭﺩﮐﻪﻣﺮﺑﻊ ﮐﺎﻣﻞ ﺑﺎﺷﺪ ﻭﺍﮔﺮ ﻳﮏ ﻭﺍﺣﺪ ﺑﻪ ﺭﻗﻢ ﺻﺪﮔﺎﻥ،ﺩﻭ
ﻭﺍﺣﺪ ﺑﻪ ﺭﻗﻢ ﺩﻫﮕﺎﻥ ﻭ ﺳﻪﻭﺍﺣﺪ ﺑﻪ ﺭﻗﻢ ﻳﮑﺎﻥ ﺁﻥ ﺍﺿﺎﻓﻪ ﺷﻮﺩ،ﺣﺎﺻﻞﺳﻪ ﺭﻗﻤﯽ ﻭﻣﺮﺑﻊﮐﺎﻣﻞ ﺑﺎﺷﺪ؟
۱(ﺻﻔﺮ٢(ﻳﮏ٣(ﺩﻭ٤(ﺳﻪ٥(ﭼﻬﺎﺭ""",
""".ﺑﺎ ﺍﺳﺘﻔﺎﺩﻩ ﺍﺯ ﻫﻤﺔﺍﺭﻗﺎﻡ۱ﺗﺎ۹،ﺳﻪﻋﺪﺩ ﺳﻪﺭﻗﻤﯽ ﺑﺎ ﺍﺭﻗﺎﻡ ﻣﺘﻤﺎﻳﺰ ﺳﺎﺧﺘﻪﺍﻳﻢ ﻭ ﺑﺰﺭﮒﺗﺮﻳﻦ ﺁﻥﻫﺎ ﺭﺍ
Aﻧﺎﻣﻴﺪﻩﺍﻳﻢ. ﮐﻢﺗﺮﻳﻦ ﻣﻘﺪﺍﺭ ﻣﻤﮑﻦ ﺑﺮﺍﯼAﭼﻨﺪ ﺍﺳﺖ؟
۱(۳۴۵٢(۱۹۸٣(۹۱۲٤(۳۹۸٥(۳۱۲""",
""".ﺑﺮﺍﯼ,A B  ﻣﯽ ﺗﻌﺮﻳﻒﮐﻨﻴﻢ{ | , }A B ab a A b B   ﭼﻨﺪﺍﺯ ﺗﺎ
ﮔﺰﺍﺭﻩﻫﺎﯼ ﺯﻳﺮ ﺩﺭﺳﺖ ﺍﺳﺖ؟)ﻧﻤﺎﺩ ﻣﺠﻤﻮﻋﺔﺍﻋﺪﺍﺩ ﮔﻨﮓ ﺍﺳﺖ.(
{ }    0  
{ , } { }  2 5 0 
    
{ , } { }  2 3 0 
۱(ﭼﻬﺎﺭ٢(ﺳﻪ٣(ﺩﻭ٤(ﻳﮏ٥(ﺻﻔﺮ""",
""".ﻣﺜﻠﺜﯽﻣﺘﺴﺎﻭﯼﺍﻻﺿﻼﻉ ﺑﻪ ﺿﻠﻊ ﻭﺍﺣﺪ ﺩﺭﻭﻥ ﻭ ﺭﻭﯼ
ﻣﺤﻴﻂ ﻳﮏ ﻣﺴﺘﻄﻴﻞ2 4،ﻣﺎﻧﻨﺪ ﺷﮑﻞ،ﻣﯽﻏﻠﻄﺪ.
ﺭﺃﺱP، ﮐﻪ ﺩﺭ ﺷﮑﻞ ﻣﺸﺨﺺ ﺷﺪﻩ،ﺍﺯ ﺍﺑﺘﺪﺍﯼ ﺣﺮﮐﺖ
ﺗﺎ ﺯﻣﺎﻧﯽ ﮐﻪﺑﺮﺍﯼ ﺍﻭﻟﻴﻦ ﺑﺎﺭﺑﻪ ﻣﮑﺎﻥ ﺍﻭﻟﻴﻪﺍﺵ ﺑﺎﺯﮔﺮﺩﺩ،
ﭼﻪ ﻣﺴﺎﻓﺘﯽ ﺭﺍ ﻃﯽ ﻣﯽﮐﻨﺪ؟
۱(
10
3
٢(3٣(4٤(
7
3
٥(2""",
""".ﭼﻨﺪ ﺳﻪﺗﺎﻳﯽ ﻣﺮﺗﺐ( , , )x y zﻭﺟﻮﺩ ﺩﺍﺭﺩ ﮐﻪ, ,x y zﺍﺭﻗﺎﻡ ﻧﺎﺻﻔﺮ ﻭ ﻣﺘﻤﺎﻳﺰﯼ ﺑﺎﺷﻨﺪ ﻭx yﺑﺮ
zﺑﺨﺶﭘﺬﻳﺮ ﺑﺎﺷﺪ؟
۱(۱۴۰٢(۱۴۴٣(۱۴۸٤(۱۵۲٥(١٥٦
""",
""".ﺍﻋﺪﺍﺩ١،٢ﻭ ...،1395ﺭﻭﯼ ﺗﺨﺘﻪ ﻧﻮﺷﺘﻪ ﺷﺪﻩ ﻭ ﻣﺎ ﺑﻪ ﺍﻳﻦ ﺷﮑﻞ ﺁﻥﻫﺎ ﺭﺍ ﺧﻂ ﻣﯽﺯﻧﻴﻢ:ﻫﺮﺑﺎﺭ
ﺑﺰﺭﮒﺗﺮﻳﻦ ﻋﺪﺩﯼﮐﻪ ﺗﺎ ﻗﺒﻞ ﺍﺯ ﺁﻥ ﺧﻂ ﻧﺨﻮﺭﺩﻩ ﺭﺍ ﺍﻧﺘﺨﺎﺏ ﻭ ﻫﻤﺔﻣﻘﺴﻮﻡ ﻋﻠﻴﻪﻫﺎﯼ ﺁﻥ ﺭﺍ ﺑﻪﺗﺮﺗﻴﺐ ﺍﺯ
ﺑﺰﺭﮒ ﺑﻪ ﮐﻮﭼﮏ ﺧﻂ ﻣﯽﺯﻧﻴﻢ ﻭ ﺳﭙﺲ ﻣﺠﺪﺩﴽﺑﻪ ﺳﺮﺍﻍ ﺑﺰﺭﮒﺗﺮﻳﻦ ﻋﺪﺩ ﺧﻂﻧﺨﻮﺭﺩﻩﻣﯽﺭﻭﻳﻢ ﻭ ﻫﻤﻴﻦ
ﮐﺎﺭﺭﺍ ﺗﮑﺮﺍﺭ ﻣﯽﮐﻨﻴﻢ ﺗﺎ ﻫﻤﺔﺍﻋﺪﺍﺩ ﺧﻂ ﺑﺨﻮﺭﻧﺪ. ﺁﺧﺮﻳﻦ ﻋﺪﺩﯼ ﮐﻪ ﺧﻂ ﻣﯽﺧﻮﺭﺩﮐﺪﺍﻡ ﺍﺳﺖ؟
۱(۳۷٢(٤١٣(٦٩٨٤(٧٠١٥(٧٠٣""",
""".ﻋﻤﻞﺭﺍ ﺩﺭ ﻣﺠﻤﻮﻋﺔﺍﻋﺪﺍﺩ ﺣﻘﻴﻘﯽ ﺑﻪ ﺻﻮﺭﺕ ﺯﻳﺮ ﺗﻌﺮﻳﻒ ﻣﯽﮐﻨﻴﻢ:
1
x y
x y xy

  
ﺍﮔﺮ, ,a b cﺭﻳﺸﻪﻫﺎﯼ3 2
3 2 5 0x x x   ﺑﺎﺷﻨﺪ، ﻣﻘﺪﺍﺭ( )a b c ﮐﺪﺍﻡ ﺍﺳﺖ؟
۱(۲٢(
2
3
٣(8٤(
8
3
٥(2""",
""".ﺗﻌﺪﺍﺩ ﺳﻪﺗﺎﻳﯽﻫﺎﯼ ﻣﺮﺗﺐ( , , )a b cﺍﺯ ﺍﻋﺪﺍﺩ ﻃﺒﻴﻌﯽ ﺭﺍ ﺑﻴﺎﺑﻴﺪ ﮐﻪ ﺩﺭ ﺷﺮﻁ ﺯﻳﺮ ﺻﺪﻕ ﮐﻨﻨﺪ:
( , ) ( , ) ( , )a b c b c a c a b    6 8 10
2 3 5
)ﻣﻨﻈﻮﺭ ﺍﺯ( , )a bﺑﺰﺭﮒﺗﺮﻳﻦ ﻣﻘﺴﻮﻡ ﻋﻠﻴﻪ ﻣﺸﺘﺮﮎaﻭbﺍﺳﺖ.(
۱(۳۲۴۰٢(٢٠٨٠٣(٢٠٠٠٤(١٦٢٠٥(۷۲۰""",
""".ﻣﯽﺧﻮﺍﻫﻴﻢﺑﺎﭼﻴﺪﻥ۱۲ﺁﺟﺮﻣﮑﻌﺒﯽﺑﻪﺿﻠﻊ ﻭﺍﺣﺪ، ﺑﺮ ﺭﻭﯼﻣﻴﺰ،ﻣﮑﻌﺐ ﻣﺴﺘﻄﻴﻠﯽﺑﻪ ﻃﻮﻝ۳،
ﻋﺮﺽ۲ﻭﺍﺭﺗﻔﺎﻉ۲ﻭﺍﺣﺪ، ﺑﺴﺎﺯﻳﻢ.ﻃﺒﻴﻌﺘﴼ ﻳﮏ ﻣﮑﻌﺐ ﺑﺎﻻﻳﯽ ﺭﺍ ﻧﻤﯽﺗﻮﺍﻥ ﻗﺒﻞ ﺍﺯ ﻣﮑﻌﺐ ﺯﻳﺮﯼ،ﺳﺮ
ﺟﺎﻳﺶﮔﺬﺍﺷﺖ.ﺑﻪ ﭼﻨﺪ ﺭﻭﺵ ﻣﺘﻔﺎﻭﺕ ﻣﯽﺗﻮﺍﻥ ﺍﻳﻦ ﻣﮑﻌﺐ ﻣﺴﺘﻄﻴﻞ ﺭﺍ ﺳﺎﺧﺖ؟)ﺗﻮﺟﻪ ﺩﺍﺷﺘﻪﺑﺎﺷﻴﺪ
ﮐﻪ ﻣﮑﻌﺐﻫﺎ ﺍﺯ ﻧﻈﺮ ﻣﺎ ﺗﻔﺎﻭﺗﯽ ﻧﺪﺍﺭﻧﺪ ﻭ ﻣﺴﺄﻟﻪ ﺗﺮﺗﻴﺐﭘﺮ ﮐﺮﺩﻥ۱۲ﻣﺤﻞ ﻣﮑﻌﺐ ﻣﺴﺘﻄﻴﻞ ﺍﺳﺖ.(
۱(۳۶٢(۱۴۴٣(۳۲۴٤(۹۲۴٥(۷۴۸۴۴۰۰""",
"""., ,a b cﺍﻋﺪﺍﺩﯼ ﺩﻭ ﺑﻪ ﺩﻭ ﻣﺘﻤﺎﻳﺰﻧﺪ. ﻣﯽﺩﺍﻧﻴﻢﺳﻪ ﻣﻌﺎﺩﻟﺔﺩﺭﺟﻪ ﺩﻭﯼ ﺯﻳﺮﺭﻳﺸﻪﺍﯼ ﻣﺸﺘﺮﮎ ﺩﺍﺭﻧﺪ.
, ,ax bx c bx cx a cx ax b        2 2 2
0 0 0
ﻣﻘﺪﺍﺭ ﺁﻥ ﺭﻳﺸﺔﻣﺸﺘﺮﮎﭼﻨﺪ ﺍﺳﺖ؟
۱(۰٢(
1 5
2
٣(1٤(١٥(ﺑﻪﻃﻮﺭ ﻳﮏﺗﺎ ﺗﻌﻴﻴﻦ ﻧﻤﯽﺷﻮﺩ.
""",
""".۱۰۰۰ﻋﺪﺩ ﺳﻴﺐﺩﺍﺭﻳﻢ ﮐﻪ۹۰۰ﻋﺪﺩﺁﻥﻫﺎﺳﺎﻟﻢﻭ ﻣﺎﺑﻘﯽﻟﮑﻪﺩﺍﺭﻫﺴﺘﻨﺪ. ﺁﻥﻫﺎ ﺭﺍﺩﺭﺗﻌﺪﺍﺩﯼﺟﻌﺒﻪ
ﭘﺨﺶﻣﯽﮐﻨﻴﻢﺑﻪﻃﻮﺭﯼ ﮐﻪ ﺗﻌﺪﺍﺩ ﺳﻴﺐﻫﺎ ﺩﺭ ﻫﺮ ﺟﻌﺒﻪ ﺑﺎ ﺟﻌﺒﺔ ﺩﻳﮕﺮ ﺑﺮﺍﺑﺮ ﺑﺎﺷﺪ.ﺩﺭﺣﺪﺍﻗﻞ ﻭ ﺣﺪﺍﮐﺜﺮ
ﭼﻨﺪﺩﺭﺻﺪﺟﻌﺒﻪﻫﺎ ﺍﮐﺜﺮﻳﺖ ﺳﻴﺐﻫﺎ ﺳﺎﻟﻢﺍﺳﺖ؟
۱(٥٠ﻭ٩٠٢(٥٠ﻭ١٠٠٣(٨٠ﻭ٩٠٤(٨٠ﻭ١٠٠٥(٩٠ﻭ١٠٠""",
"""ﭼﻨﺪ ﺯﻭﺝ ﻣﺮﺗﺐ( , )m nﺍﺯ ﺍﻋﺪﺍﺩ ﻃﺒﻴﻌﯽ ﺩﺍﺭﻳﻢ ﮐﻪ1 2 1395 1 2[ , ,..., ] [ , ,..., ]m n .
)ﻣﻨﻈﻮﺭ ﺍﺯﻧﻤﺎﺩ1 2[ , ,..., ]mﮐﻮﭼﮏﺗﺮﻳﻦ ﻣﻀﺮﺏ ﻣﺸﺘﺮﮎﻣﺜﺒﺖﺍﻋﺪﺍﺩ1 2, ,...,mﺍﺳﺖ.(
۱(ﺻﻔﺮ٢(ﻳﮏ٣(ﺩﻭ٤(ﺳﻪ٥(ﭼﻬﺎﺭ""",
""".ﻳﮏ ﻣﻨﺸﻮﺭ ﻗﺎﺋﻢ ﺑﺎ ﻗﺎﻋﺪﺓﺷﺶﺿﻠﻌﯽ ﻣﻨﺘﻈﻢ ﺑﻪ ﺿﻠﻊ ﻭﺍﺣﺪ ﺭﺍ ﺗﻮﺳﻂ ﻳﮏ
ﺻﻔﺤﻪﺑﺮﺵ ﺯﺩﻩﺍﻳﻢ. ﺍﮔﺮ ﻓﺎﺻﻠﺔﺭﺋﻮﺱﺍﻳﻦ ﺳﻄﺢ ﻣﻘﻄﻊ ﺗﺎ ﻗﺎﻋﺪﺓﭘﺎﻳﻴﻦ
ﺑﻪﺗﺮﺗﻴﺐ ﺑﺮﺍﺑﺮ٢،٣،x،y،١١ﻭzﺑﺎﺷﺪx y z ﭼﻪﻗﺪﺭ ﺍﺳﺖ؟
۱(۱۶٢(۱۸٣(۲۰
٤(۲۴٥(۲۶""",
""".ﺩﺭ ﺷﻬﺮ ﺳﺎﺩﻩﻟﻮﺣﺎﻥ ﺷﺎﻳﻌﻪﻫﺎ ﺑﻪﺳﺮﻋﺖﭘﺨﺶ ﻣﯽﺷﻮﺩ؛ﺍﮔﺮﺁﻗﺎﯼ
ﺧﺎﻟﯽﺑﻨﺪ،ﺑﺨﻮﺍﻫﺪﺷﺎﻳﻌﻪﺍﯼ ﺭﺍ ﭘﺨﺶ ﮐﻨﺪﺍﺑﺘﺪﺍﺁﻥﺷﺎﻳﻌﻪﺭﺍ ﺑﻪ ﻳﮏ ﻧﻔﺮ
ﺩﻳﮕﺮ ﻣﻨﺘﻘﻞ ﻣﯽﮐﻨﺪ. ﺩﺭﺍﺩﺍﻣﻪ ﻫﺮ ﺭﻭﺯﺁﻗﺎﯼ ﺧﺎﻟﯽﺑﻨﺪ ﻭﻫﺮ ﮐﺴﯽ ﮐﻪ
ﺷﺎﻳﻌﻪﺭﺍ ﺩﺭ ﻳﮑﯽ ﺍﺯ ﺭﻭﺯﻫﺎﯼ ﮔﺬﺷﺘﻪ ﺷﻨﻴﺪﻩ ﺁﻥ ﺭﺍ ﺑﻪ ﻓﺮﺩ ﺟﺪﻳﺪﯼ
ﻣﻨﺘﻘﻞ ﻣﯽﮐﻨﺪ.ﭘﺲ ﺍﺯ ﺁﻥﮐﻪ ﺗﻌﺪﺍﺩ ﺍﻓﺮﺍﺩﯼ ﮐﻪ ﺷﺎﻳﻌﻪ ﺭﺍ ﺷﻨﻴﺪﻩﺍﻧﺪ ﺍﺯ
ﻣﺮﺯ ﻳﮏ ﻣﻴﻠﻴﻮﻥ ﻧﻔﺮﮔﺬﺷﺖ، ﭼﻨﺪ ﻧﻔﺮ ﺷﺎﻳﻌﻪ ﺭﺍ ﻣﺴﺘﻘﻴﻤﴼﻳﺎ ﺑﺎ ﻳﮏ ﻭﺍﺳﻄﻪﺍﺯ ﺁﻗﺎﯼ ﺧﺎﻟﯽﺑﻨﺪ ﺷﻨﻴﺪﻩﺍﻧﺪ؟
۱(۲۰٢(٢١٠٣(١٠٢٤٤(٥٠٠٠٠٠٥(٥٢٤٢٨٨""",
""".ﭼﻨﺪ ﺯﻭﺝ ﻣﺮﺗﺐ ﺍﺯ ﺍﻋﺪﺍﺩ ﺣﻘﻴﻘﯽ( , )x yﻭﺟﻮﺩ ﺩﺍﺭﺩ ﮐﻪ ﺩﺭ ﺩﺳﺘﮕﺎﻩ ﻣﻌﺎﺩﻻﺕ ﺯﻳﺮ ﺻﺪﻕﮐﻨﺪ؟
x xy y x y
x xy y x y
     
     
2 2
2 2
3 2 0
2 2 3 2 5 0
۱(۲٢(٣٣(٤٤(٥٥(٦""",
""".ﺧﻴﺎﺑﺎﻥﻣﺤﻠﻪ ﮐﺸﯽﺷﮑﻞ ﺑﻪ ﺍﯼ
ﺭﻭﺑﻪﺭﻭ ﺍﺳﺖ: ﺳﻪ ﺧﻴﺎﺑﺎﻥ ﺍﻓﻘﯽ ﻭ ﺩﻩ
ﺧﻴﺎﺑﺎﻥ ﻋﻤﻮﺩﯼ. ﭘﻠﻴﺴﯽ ﻣﯽﺧﻮﺍﻫﺪ ﺑﻪ
ﻫﻤﺔ ﺗﻘﺎﻃﻊﻫﺎ ﺳﺮﮐﺸﯽ ﮐﻨﺪ ﺑﻪﻃﻮﺭﯼ
ﮐﻪ ﺍﺯ ﺗﻘﺎﻃﻊ ﺭﺍﺳﺖ-ﺑﺎﻻ ﺷﺮﻭﻉ ﮐﻨﺪ، ﺍﺯ ﻫﺮ ﺗﻘﺎﻃﻊ ﺩﻗﻴﻘﴼ ﻳﮏ ﺑﺎﺭ ﻋﺒﻮﺭ ﮐﻨﺪ ﻭ ﺩﺭ ﺍﻧﺘﻬﺎ ﺑﻪ ﺗﻘﺎﻃﻊ ﺭﺍﺳﺖ-
ﺑﺎﻻ ﺑﺮﮔﺮﺩﺩ. ﺍﻳﻦ ﮐﺎﺭ ﺑﻪ ﭼﻨﺪ ﺭﻭﺵﻣﺨﺘﻠﻒﻣﻤﮑﻦ ﺍﺳﺖ؟
۱(5
2٢(5
3٣( 4
2 3٤(4
2٥(6 5
3 3""",
""".ﺧﻴﺎﺑﺎﻥﻫﺎﯼﻣﺤﻠﻪﺍﯼ ﺑﻪ ﻧﺎﻡ ﭘﻬﺮﺍﻥ ﻣﺎﻧﻨﺪ ﺷﮑﻞﺭﻭﺑﻪﺭﻭﺷﺎﻣﻞ۹ﺗﻘﺎﻃﻊ ﻭ۱۲
ﺧﻴﺎﺑﺎﻥ ﺍﺳﺖ. )ﻣﺴﻴﺮ ﺑﻴﻦ ﻫﺮ ﺩﻭ ﺗﻘﺎﻃﻊ ﻳﮏ ﺧﻴﺎﺑﺎﻥﺍﺳﺖ.(ﻫﺮﺷﺐﺩﺭ ﺍﻳﻦﻣﺤﻠﻪ
۹۰ﺧﻮﺩﺭﻭﭘﺎﺭﮎﻣﯽﺷﻮﺩﮐﻪ ﻫﻤﮕﯽ ﺩﺍﺧﻞ ﺧﻴﺎﺑﺎﻥﻫﺎ ﻭ ﻧﻪ ﺩﺭ ﺗﻘﺎﻃﻊﻫﺎﻗﺮﺍﺭ ﺩﺍﺭﻧﺪ.
ﺩﺭ ﻫﺮﺗﻘﺎﻃﻊ ﻣﻴﺎﻧﮕﻴﻦ ﺗﻌﺪﺍﺩ ﺧﻮﺩﺭﻭﻫﺎﯼ ﻣﻮﺟﻮﺩ ﺩﺭ ﺧﻴﺎﺑﺎﻥﻫﺎﯼﻣﺘﺼﻞﺑﻪﺁﻥ
ﺗﻘﺎﻃﻊﺭﺍﻇﺮﻓﻴﺖ ﭘﺎﺭﮎ ﺁﻥ ﺗﻘﺎﻃﻊ ﻣﯽﻧﺎﻣﻴﻢ.ﻣﯽﺩﺍﻧﻴﻢﮐﻪﻣﺠﻤﻮﻉﻇﺮﻓﻴﺖ ﭘﺎﺭﮎ۹ﺗﻘﺎﻃﻊ،ﺑﺮﺍﺑﺮ۶۶
ﺍﺳﺖ. ﮐﺪﺍﻡ ﻳﮏ ﺍﺯ ﮔﺰﺍﺭﻩﻫﺎﯼ ﺯﻳﺮ ﺣﺘﻤﴼﺩﺭﺳﺖ ﺍﺳﺖ؟
۱(ﻇﺮﻓﻴﺖ ﭘﺎﺭﮎ ﺗﻘﺎﻃﻊ ﻣﺮﮐﺰﯼ ﻣﺤﻠﻪ، ﺑﻴﺶﺗﺮ ﺍﺯ ﺗﻘﺎﻃﻊﻫﺎﯼ ﺩﻳﮕﺮ ﺍﺳﺖ.
۲(ﺩﺭ ﻫﺮ ﻳﮏ ﺍﺯ ﺧﻴﺎﺑﺎﻥﻫﺎﻳﯽ ﮐﻪ ﺩﺭ ﺣﺎﺷﻴﺔ ﻣﺤﻠﻪ ﻭﺍﻗﻊ ﺍﺳﺖ، ﺩﺳﺖﮐﻢ۶ﺧﻮﺩﺭﻭ ﭘﺎﺭﮎ ﺷﺪﻩ ﺍﺳﺖ.
۳(ﺩﺭ ﻳﮑﯽ ﺍﺯ ﺧﻴﺎﺑﺎﻥﻫﺎﻳﯽ ﮐﻪ ﺩﺭ ﺣﺎﺷﻴﺔ ﻣﺤﻠﻪ ﻭﺍﻗﻊ ﺍﺳﺖ، ﺩﺳﺖﮐﻢ۸ﺧﻮﺩﺭﻭ ﭘﺎﺭﮎ ﺷﺪﻩ ﺍﺳﺖ.
۴(ﺩﺭ ﻳﮑﯽ ﺍﺯ ﺧﻴﺎﺑﺎﻥﻫﺎﯼ ﻣﺘﺼﻞ ﺑﻪ ﻣﺮﮐﺰ ﻣﺤﻠﻪ، ﺩﺳﺖﮐﻢ۹ﺧﻮﺩﺭﻭ ﭘﺎﺭﮎ ﺷﺪﻩ ﺍﺳﺖ.
۵(ﮔﺰﻳﻨﻪﻫﺎﯼ۱ﻭ۴.""",
""".ﺩﺭ ﻣﺴﺎﺑﻘﺔﻗﻮﯼﺗﺮﻳﻦ ﻣﺮﺩﺍﻥ ﺍﻳﺮﺍﻥ۱۰ﺧﺎﻧﻪ ﺩﻭﺭ ﻳﮏ ﺩﺍﻳﺮﻩ ﻗﺮﺍﺭ
ﺩﺍﺭﺩ ﮐﻪ ﺩﺭ ﻫﺮ ﺧﺎﻧﻪ۲۰۰ﻭﺯﻧﻪ ﺍﺯ ﻫﻤﺔﻭﺯﻧﻪﻫﺎﯼ۱،۲ﻭ ...،۲۰۰
ﮐﻴﻠﻮﮔﺮﻣﯽﻭﺟﻮﺩ ﺩﺍﺭﺩ. ﺍﺑﺘﺪﺍ ﻣﺮﺩﯼ ﺩﺭ ﺧﺎﻧﻪﺍﯼ ﻗﺮﺍﺭ ﺩﺍﺭﺩ، ﺑﺎ ﺷﺮﻭﻉ
ﻣﺴﺎﺑﻘﻪ ﺍﺯ ﺁﻥ ﺧﺎﻧﻪ ﻭﺯﻧﺔ۱ﮐﻴﻠﻮﮔﺮﻣﯽ ﺭﺍ ﺑﺮﺩﺍﺷﺘﻪ ﻭ ﺩﺭ ﺟﻬﺖ
ﻋﻘﺮﺑﻪﻫﺎﯼ ﺳﺎﻋﺖ ﺣﺮﮐﺖ ﮐﺮﺩﻩ۱ﺧﺎﻧﻪ ﺑﻪ ﺟﻠﻮ ﻣﯽﺭﻭﺩ، ﻭﺯﻧﻪ ﺭﺍ
ﺩﺭ ﺁﻥﺟﺎ ﻗﺮﺍﺭ ﺩﺍﺩﻩ ﻭ ﺍﺯ ﺁﻥ ﺧﺎﻧﻪ ﻭﺯﻧﺔ۲ﮐﻴﻠﻮﮔﺮﻣﯽ ﺭﺍ ﺑﺮﺩﺍﺷﺘﻪ ﻭ۲ﺧﺎﻧﻪ ﺑﻪ ﻋﻘﺐ )ﭘﺎﺩﺳﺎﻋﺖﮔﺮﺩ( ﺁﻣﺪﻩ
ﻭ ﻭﺯﻧﻪ ﺭﺍ ﺩﺭ ﺁﻥ ﻗﺮﺍﺭ ﻣﯽﺩﻫﺪ، ﺳﭙﺲﺍﺯ ﺁﻥﺟﺎﻭﺯﻧﺔ۳ﮐﻴﻠﻮﮔﺮﻣﯽ ﺭﺍﺑﺮﺩﺍﺷﺘﻪ۳ﺧﺎﻧﻪ ﺩﺭ ﺟﻬﺖ
ﺳﺎﻋﺖﮔﺮﺩﻣﯽﺭﻭﺩ ﻭﻫﻤﻴﻦ ﺭﻭﻧﺪ ﺍﺩﺍﻣﻪ ﻣﯽﻳﺎﺑﺪ.ﭘﺲ ﺍﺯ ﺁﻥﮐﻪ ﻭﺯﻧﺔ۲۰۰ﮐﻴﻠﻮﮔﺮﻣﯽ ﺭﺍ ﺟﺎﺑﻪﺟﺎ ﮐﺮﺩ ﺩﺭ
ﺧﺎﻧﻪﺍﯼ ﮐﻪ ﮐﺎﺭ ﺧﻮﺩ ﺭﺍ ﺍﺯ ﺁﻥﺟﺎ ﺷﺮﻭﻉ ﮐﺮﺩﻩﺑﻮﺩ ﻣﺠﻤﻮﻋﴼﭼﻨﺪ ﮐﻴﻠﻮﮔﺮﻡ ﻭﺯﻧﻪ ﻭﺟﻮﺩ ﺩﺍﺭﺩ؟
۱(۲۰۲۸۰٢(٢٠٢٠٠٣(٢٠١٨٠٤(٢٠١٠٠٥(٢٠٠٨٠
""",
""".ﻣﺜﻠﺚABCﻣﻔﺮﻭﺽ ﺍﺳﺖ. ﻓﺮﺽ ﮐﻨﻴﺪbwﻭcwﺑﻪﺗﺮﺗﻴﺐ ﺩﻭ ﺩﺍﻳﺮﺓﮔﺬﺭﻧﺪﻩ ﺍﺯAﺑﺎﺷﻨﺪ ﺑﻪ
ﻃﻮﺭﯼ ﮐﻪ ﺑﻪﺗﺮﺗﻴﺐ ﺩﺭBﻭCﺑﺮBCﻣﻤﺎﺱ ﺑﺎﺷﻨﺪﻭNﻭAﻣﺤﻞ ﺑﺮﺧﻮﺭﺩ ﺩﻭ ﺩﺍﻳﺮﺓﻣﺬﮐﻮﺭ
ﺑﺎﺷﻨﺪ. ﺍﺯ ﻫﺮ ﮐﺪﺍﻡﺍﺯ ﻧﻘﺎﻁBﻭCﺧﻄﯽ ﻣﻮﺍﺯﯼ ﺑﺎ ﺿﻠﻊ ﺭﻭﺑﻪﺭﻭﻳﺶ ﺭﺳﻢ ﻣﯽﮐﻨﻴﻢ ﻭ ﻣﺤﻞ ﺑﺮﺧﻮﺭﺩ
ﺍﻳﻦ ﺩﻭ ﺧﻂ ﺭﺍTﻧﺎﻡﮔﺬﺍﺭﯼ ﻣﯽﮐﻨﻴﻢ.ﮔﻴﺮﻳﻢﺧﻄﻮﻁTCﻭTBﺑﻪﺗﺮﺗﻴﺐ ﺩﺍﻳﺮﻩﻫﺎﯼﻣﺤﻴﻄﯽ
ﻣﺜﻠﺚﻫﺎﯼANCﻭANBﺭﺍ ﺑﺮﺍﯼ ﺑﺎﺭ ﺩﻭﻡ ﺩﺭEﻭFﻗﻄﻊ ﮐﻨﻨﺪ. ﺍﮔﺮ8BC ﻭ
6AN ،ﺣﺎﺻﻞNF NEﮐﺪﺍﻡ ﺍﺳﺖ؟
۱(۶۴٢(٨١٣(١٠٠٤(١٥٠٥(٢٠٠""",
""".ﺩﺭ ﻣﺘﻮﺍﺯﯼﺍﻻﺿﻼﻉABCDﺩﺍﺭﻳﻢ60ABC  
.Eﺭﺍ ﻧﻘﻄﻪﺍﯼ ﺭﻭﯼABﺑﮕﻴﺮﻳﺪ ﮐﻪ
BE AE 2، ﺑﻪﻋﻼﻭﻩFﺭﺍ ﻫﻢ ﻗﺮﻳﻨﺔEﻧﺴﺒﺖ ﺑﻪ ﻣﺮﮐﺰ ﻣﺘﻮﺍﺯﯼﺍﻻﺿﻼﻉ ﻓﺮﺽ ﮐﻨﻴﺪ. ﺍﮔﺮBF
ﻭCEﺑﺮﻫﻢ ﻋﻤﻮﺩ ﺑﺎﺷﻨﺪ، ﻧﺴﺒﺖﺿﻠﻊ ﮐﻮﭼﮏﺗﺮ ﺑﻪ ﺿﻠﻊ ﺑﺰﺭﮒﺗﺮﻣﺘﻮﺍﺯﯼﺍﻻﺿﻼﻉ ﺑﻪ ﮐﺪﺍﻡ ﮔﺰﻳﻨﻪ
ﻧﺰﺩﻳﮏﺗﺮ ﺍﺳﺖ؟
۱(/0 2۲(/0 3۳(/0 4۴(/0 5٥(/0 6""",
""".ﺑﺰﺭﮒﺗﺮﻳﻦ ﻋﺪﺩ ﺣﻘﻴﻘﯽ ﻭ ﺛﺎﺑﺖkﺭﺍ ﺑﻴﺎﺑﻴﺪ ﺑﻪﻃﻮﺭﯼ ﮐﻪ ﺑﺮﺍﯼ ﺗﻤﺎﻡ ﺍﻋﺪﺍﺩ ﺣﻘﻴﻘﯽ, , , ,a b c d e:
2 2 2 2 2 2
( ) ( ) ( ) ( ) ( ) ( )a b b c c d d e e a k b d          
۱(۱٢(0 5/٣(
1
6
٤(٢٥(
5
6""",
""".ﺑﺮﺍﯼ ﺯﻳﺮﻣﺠﻤﻮﻋﺔ ﻧﺎﺗﻬﯽAﺍﺯ ﻧﻘﺎﻁ ﺻﻔﺤﻪ ﻭ ﻋﺪﺩ ﺣﻘﻴﻘﯽ0r ، ﻣﺠﻤﻮﻋﺔ ﻧﻘﺎﻃﯽ ﮐﻪ ﺍﺯ ﺩﺳﺖﮐﻢ
ﻳﮏ ﻧﻘﻄﺔAﻓﺎﺻﻠﻪﺍﯼ ﮐﻢﺗﺮ ﻳﺎ ﻣﺴﺎﻭﯼrﺩﺍﺭﻧﺪ ﺭﺍ ﺑﺎrAﻧﻤﺎﻳﺶ ﻣﯽﺩﻫﻴﻢ. ﭼﻨﺪ ﺗﺎ ﺍﺯ ﮔﺰﺍﺭﻩﻫﺎﯼ ﺯﻳﺮ
ﺩﺭﺳﺖ ﻫﺴﺘﻨﺪ؟ )ﺩﺭ ﻫﻤﺔ ﻣﻮﺍﺭﺩrﻭsﺍﻋﺪﺍﺩ ﺣﻘﻴﻘﯽ ﻣﺜﺒﺖ ﻭAﻭBﺯﻳﺮﻣﺠﻤﻮﻋﻪﻫﺎﻳﯽ ﺍﺯ ﺻﻔﺤﻪ
ﻫﺴﺘﻨﺪ.(
( ) ( )r s s rA A.
rA Bﺍﮔﺮ ﻭ ﺗﻨﻬﺎ ﺍﮔﺮrB A.
ﺍﮔﺮ ﺑﺮﺍﯼ ﻫﺮ0t ،t tA BﺁﻥﮔﺎﻩA B.
( )r r rA B A B  .
ﺍﮔﺮA Bﻧﺎﺗﻬﯽ ﺑﺎﺷﺪ ﺩﺍﺭﻳﻢ( )r r rA B A B  .
۱(ﻳﮏ٢(ﺩﻭ٣(ﺳﻪ٤(ﭼﻬﺎﺭ٥(ﭘﻨﺞ
""",
""".ﺩﺭ ﻣﺜﻠﺚABCﺩﺍﺭﻳﻢ2ˆ ˆB C.ﻋﻤﻮﺩﻣﻨﺼﻒ ﺿﻠﻊBCﺩﺭ ﻧﻘﻄﺔDﺑﺎ ﺿﻠﻊAC
ﺑﺮﺧﻮﺭﺩ ﻣﯽﮐﻨﺪ ﻭ ﻋﻤﻮﺩﻣﻨﺼﻒBDﺩﺭ ﻧﻘﻄﺔFﺑﺎ ﺿﻠﻊABﺗﻘﺎﻃﻊ ﺩﺍﺭﺩ. ﺩﺍﻳﺮﻩﺍﯼ ﮐﻪ ﻣﺮﮐﺰ ﺁﻥ
ﺭﻭﯼ ﺧﻂFDﺍﺳﺖ ﺭﺍ ﺧﺎﺭﺝ ﺍﺯ ﻣﺜﻠﺚ ﺩﺭ ﻧﻈﺮ ﻣﯽﮔﻴﺮﻳﻢ ﮐﻪ ﺑﺮ ﺿﻠﻊACﻭ ﺍﻣﺘﺪﺍﺩ ﺿﻠﻊBC
ﻣﻤﺎﺱ ﺷﻮﺩ. ﺍﮔﺮ ﻣﺴﺎﺣﺖ ﻣﺜﻠﺚABCﻧﻪﺑﺮﺍﺑﺮ ﻣﺴﺎﺣﺖ ﻣﺜﻠﺚAFDﺑﺎﺷﺪﻭFO  4، ﺷﻌﺎﻉ
ﺩﺍﻳﺮﻩﭼﻪﻗﺪﺭﻣﯽﺷﻮﺩ؟
۱(3 3٢(3 3٣(3 2٤(3 2٥(2 6""",
""".ﻓﺮﺽ ﮐﻨﻴﺪ, ,x y zﺍﻋﺪﺍﺩ ﺣﻘﻴﻘﯽ ﻣﺜﺒﺖ ﺑﺎﺷﻨﺪ ﺑﻪ ﮔﻮﻧﻪﺍﯼ ﮐﻪ222x y z  ﻭ
xy yz zx   12321.ﺍﮔﺮ min , ,A xy yz zxﺁﻥﮔﺎﻩ ﺑﻴﺶﺗﺮﻳﻦ ﻣﻘﺪﺍﺭ ﻣﻤﮑﻦ
ﺑﺮﺍﯼAﭼﻨﺪ ﺍﺳﺖ؟
۱(٥٤٧٦٢(٤١٠٧٣(٢٤١٢٤(١٦٠٢٥(١٣٦٩""",
""".ﺯﻳﺮﻣﺠﻤﻮﻋﻪﺍﯼﺍﺯ{ , , ,..., }0 1 2 99ﻣﺜﻞAﺭﺍ»ﺗﻘﺮﻳﺒﴼﺟﻤﻌﯽ«ﻣﯽﮔﻮﻳﻴﻢ، ﻫﺮﮔﺎﻩﺑﻴﺶ ﺍﺯ ﻳﮏﻋﻀﻮ
ﺩﺍﺷﺘﻪ ﺑﺎﺷﺪ ﻭ ﺑﻪﻋﻼﻭﻩ ﺑﺮﺍﯼﻫﺮ ﺩﻭ ﻋﻀﻮ ﻣﺘﻤﺎﻳﺰaﻭbﺍﺯA،ﺑﺎﻗﯽﻣﺎﻧﺪﺓﺗﻘﺴﻴﻢ1a b ﺑﺮ
100ﻧﻴﺰ ﻋﻀﻮﯼ ﺍﺯAﺑﺎﺷﺪ. ﭼﻨﺪﺯﻳﺮﻣﺠﻤﻮﻋﺔﺗﻘﺮﻳﺒﴼﺟﻤﻌﯽ ﻭﺟﻮﺩ ﺩﺍﺭﺩ؟
۱(٤٩٢(٩٩٣(١٤٨٤(١٥٥٥(٢٠٠""",
""".ﻭﺗﺮﻫﺎﯼABﻭCDﺍﺯ ﺩﺍﻳﺮﺓW، ﺩﺭ ﻧﻘﻄﺔPﺧﺎﺭﺝ ﺍﺯ ﺩﺍﻳﺮﻩ ﻣﺘﻘﺎﻃﻊﺍﻧﺪﮐﻪAﺑﻴﻦBﻭP
ﺍﺳﺖ ﻭCﺑﻴﻦDﻭPﺍﺳﺖ. ﻣﯽﺩﺍﻧﻴﻢAB AP 3. ﻋﻤﻮﺩﻫﺎﯼ ﻭﺍﺭﺩ ﺍﺯCﻭDﺑﺮABﺭﺍ
ﺑﻪﺗﺮﺗﻴﺐHﻭH ﻭ ﻭﺳﻂ ﭘﺎﺭﻩﺧﻂPBﺭﺍMﻣﯽﻧﺎﻣﻴﻢ.ﺍﮔﺮ3
CM
CH ﺑﺎﺷﺪ،ﻣﻘﺪﺍﺭ
DM
DH 
ﭼﻪﻗﺪﺭ ﺍﺳﺖ؟
۱(2 3٢(3 3٣(3٤(6٥(
3
2""",
        ]

class Loader1390_3(Loader):

    def load_and_split(self):
        f = open("data.txt", "r")
        text = f.read()
        text = text.replace('\x00', '')
        self.all_texts = text.split("\"\"\"")

class Loader1393(Loader):

    def load_and_split(self):
        i = 0
        for page in self.pages:
            content = page.page_content
            split_text = self.splitter.split_text(content)
            for s in split_text[1:]:
                self.all_texts.append(s)
            for s in self.all_texts:
                print(s)
                print("-----------------------------------------" + str(i))
                i += 1

# loader_1390 = Loader1390("1390")
# loader_1391 = Loader1("1391")
# loader_1392 = Loader1392("1392")
# loader_1393 = Loader1393("1393")

loader_1394 = Loader1390_3("1393")
loader_1394.load_and_split()
loader_1394.do_translation()
