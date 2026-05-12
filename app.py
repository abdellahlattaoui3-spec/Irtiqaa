<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تطبيق ارتقي - Ertaqi</title>
    <style>
        /* تعريف المتغيرات لتغيير الألوان بسهولة */
        :root {
            --primary-gold: #D4AF37;
            --main-bg: #1A1A1A;
            --text-color: #ffffff;
            --card-bg: rgba(255, 255, 255, 0.1);
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url('https://images.unsplash.com/photo-1542810634-71277d95dcbb?q=80&w=2070') no-repeat center center fixed;
            background-size: cover;
            color: var(--text-color);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* خانة تغيير الثيم (المتطرفة) */
        .theme-switcher {
            position: fixed;
            top: 20px;
            left: 20px;
            background: var(--card-bg);
            padding: 10px;
            border-radius: 10px;
            border: 1px solid var(--primary-gold);
            backdrop-filter: blur(5px);
            z-index: 1000;
        }

        .container {
            width: 90%;
            max-width: 500px;
            text-align: center;
            margin-top: 50px;
            flex-grow: 1;
        }

        /* زر المحاسبة الرئيسي */
        .main-btn {
            background: var(--primary-gold);
            color: black;
            padding: 20px 40px;
            border: none;
            border-radius: 15px;
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
            transition: 0.3s;
            margin-bottom: 30px;
        }

        /* قسم المحاسبة (مخفي في البداية) */
        #accounting-section {
            display: none;
            background: var(--card-bg);
            padding: 20px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid var(--primary-gold);
            margin-bottom: 50px;
        }

        .category-btn {
            width: 100%;
            background: rgba(255,255,255,0.05);
            color: var(--text-color);
            border: 1px solid var(--primary-gold);
            padding: 12px;
            margin: 10px 0;
            border-radius: 10px;
            text-align: right;
            cursor: pointer;
            font-size: 18px;
        }

        .sub-tasks {
            display: none;
            background: rgba(0,0,0,0.3);
            padding: 10px;
            border-radius: 10px;
            margin-top: 5px;
        }

        .task-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 0.5px solid rgba(212, 175, 55, 0.2);
        }

        /* التذييل الفخم */
        footer {
            width: 100%;
            text-align: center;
            padding: 20px 0;
            background: rgba(0,0,0,0.7);
            border-top: 2px solid var(--primary-gold);
        }

        .dua { font-size: 18px; color: white; }
        .signature { 
            color: var(--primary-gold); 
            font-weight: bold; 
            letter-spacing: 2px;
            margin-top: 5px;
        }
    </style>
</head>
<body>

    <!-- تغيير الثيم -->
    <div class="theme-switcher">
        <label>لون الخط: </label>
        <input type="color" id="textColorPicker" value="#ffffff" onchange="updateColors()">
        <br>
        <label>الثيم العام: </label>
        <input type="color" id="themeColorPicker" value="#D4AF37" onchange="updateColors()">
    </div>

    <div class="container">
        <h1 style="color: var(--primary-gold); font-size: 45px;">ارتقي</h1>
        
        <button class="main-btn" onclick="toggleSection('accounting-section')">خانة المحاسبة</button>

        <!-- قسم المحاسبة المليء بالتفاصيل -->
        <div id="accounting-section">
            
            <!-- الصلوات المفروضة -->
            <button class="category-btn" onclick="toggleSection('prayer-tasks')">➕ الصلوات الخمس (جماعة)</button>
            <div id="prayer-tasks" class="sub-tasks">
                <div class="task-item"><span>الفجر</span> <input type="checkbox"></div>
                <div class="task-item"><span>الظهر</span> <input type="checkbox"></div>
                <div class="task-item"><span>العصر</span> <input type="checkbox"></div>
                <div class="task-item"><span>المغرب</span> <input type="checkbox"></div>
                <div class="task-item"><span>العشاء</span> <input type="checkbox"></div>
            </div>

            <!-- النوافل مقسمة -->
            <button class="category-btn" onclick="toggleSection('nafila-tasks')">➕ صلوات النوافل</button>
            <div id="nafila-tasks" class="sub-tasks">
                <div class="task-item"><span>السنن الرواتب</span> <input type="checkbox"></div>
                <div class="task-item"><span>صلاة الضحى</span> <input type="checkbox"></div>
                <div class="task-item"><span>صلاة الوتر</span> <input type="checkbox"></div>
            </div>

            <!-- المهام الأخرى -->
            <button class="category-btn">🌙 قيام الليل</button>
            <button class="category-btn">📖 حفظ القرآن</button>
            <button class="category-btn">📚 الورد اليومي</button>
            <button class="category-btn">🎓 العلم الخاص (تسيير واقتصاد)</button>
            <button class="category-btn">❤️ بر الوالدين</button>
            <button class="category-btn">📿 أذكار الصباح والمساء</button>

        </div>
    </div>

    <!-- التذييل كما طلبت يا عبد الله -->
    <footer>
        <div class="dua">اللهم اغفر لي ولوالديَّ</div>
        <div class="signature">BY ABDELLAH</div>
    </footer>

    <script>
        // وظيفة لإظهار وإخفاء الأقسام
        function toggleSection(id) {
            const el = document.getElementById(id);
            el.style.display = (el.style.display === 'block') ? 'none' : 'block';
        }

        // وظيفة تغيير الثيم (العفسة التفاعلية)
        function updateColors() {
            const textColor = document.getElementById('textColorPicker').value;
            const themeColor = document.getElementById('themeColorPicker').value;
            
            document.documentElement.style.setProperty('--text-color', textColor);
            document.documentElement.style.setProperty('--primary-gold', themeColor);
        }
    </script>
</body>
</html>
