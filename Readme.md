<h1>Hướng dẫn sử dụng</h1>

<h5>B1: git  clone "https://github.com/lequoctrang4/task_backend"</h5>
<h5>B2: pip install -r requirements.txt</h5>
<h5>B3: python manage.py makemigrations</h5>
<h5>B4: python manage.py migrate</h5>
<h5>B5: .\venv\Scripts\activate</h5>
<h5>B6: python manage.py runserver</h5>
<h5>B7: Đầu tiên thì cần phải thêm category nếu database chưa có dữ liệu: bằng api /category/ (ví dụ: http://127.0.0.1:8000/category/) và sau đó thêm kiểu json như sau:</h5>
<p>{"name": "shirt"}</p>











Vui lòng bỏ qua

{
    "code": "WS12",
    "name": "Radiant Tee",
    "style": "Tee",
    "pattern": "Solid" ,
    "material": "Hemp, Spandex, Organic Cotton",
    "climate": "Indoor, Warm",
    "publish_date": "2023-07-30",
    "quantity": 100,
    "category_id": 1,
    "Details": [
        {
            "size": "M",
            "color": "pink",
            "price": 22,
            "sale_price": 22,
            "image": [
                
            ]
        },

    ]
}

