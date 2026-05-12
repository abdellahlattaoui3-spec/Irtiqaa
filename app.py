<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تطبيق ارتقي - Ertaqi</title>
    <style>
        :root {
            --primary-gold: #D4AF37;
            --text-color: #ffffff;
            --panel-bg: rgba(0, 0, 0, 0.75);
        }

        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            background: #1a1a1a no-repeat center center fixed;
            background-size: cover;
            transition: background 0.5s ease-in-out;
        }

        /* لوحة التحكم الدائرية المحسنة */
        .settings-panel {
            position: fixed;
            top: 20px;
            left: 20px;
            background: var(--panel-bg);
            padding: 20px;
            border-radius: 25px; /* شكل دائري الحواف */
            border: 2px solid var(--primary-gold);
            backdrop-filter: blur(10px);
            z-index: 1000;
            color: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }

        .settings-group {
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(212, 175,
