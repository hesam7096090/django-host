const imageInput = document.getElementById('images');

const imagePreviewContainer = document.getElementById('imagePreviewContainer');

imageInput.addEventListener('change', function () {
    // پاک کردن پیش‌نمایش‌های قبلی
    imagePreviewContainer.innerHTML = '';

    // خواندن فایل‌های انتخاب‌شده
    const files = Array.from(this.files);
    files.forEach((file, index) => {
        const reader = new FileReader();
        reader.onload = function (e) {
            // ساخت کارت پیش‌نمایش
            const imageCard = document.createElement('div');
            imageCard.classList.add('card', 'p-2');
            imageCard.style.width = '150px';
            imageCard.style.position = 'relative';

            // پیش‌نمایش تصویر
            const img = document.createElement('img');
            img.src = e.target.result;
            img.alt = file.name;
            img.classList.add('card-img-top');
            img.style.height = '100px';
            img.style.objectFit = 'cover';

            // دکمه حذف
            const removeButton = document.createElement('button');
            removeButton.classList.add('btn', 'btn-danger', 'btn-sm');
            removeButton.style.position = 'absolute';
            removeButton.style.top = '5px';
            removeButton.style.right = '5px';
            removeButton.innerText = 'حذف';
            removeButton.addEventListener('click', function () {
                files.splice(index, 1);
                imageCard.remove();

                const dataTransfer = new DataTransfer();
                files.forEach(file => dataTransfer.items.add(file));
                imageInput.files = dataTransfer.files;
            });

            imageCard.appendChild(img);
            imageCard.appendChild(removeButton);
            imagePreviewContainer.appendChild(imageCard);
        };

        reader.readAsDataURL(file);
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const tabs = document.querySelectorAll('#productTabs button');
    const nextButtons = document.querySelectorAll('.next-tab');
    const prevButtons = document.querySelectorAll('.prev-tab');

    nextButtons.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            tabs[index + 1].click();
        });
    });

    prevButtons.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            tabs[index].click();
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {


});



const provincesAndCities = {
    "آذربایجان شرقی": ["تبریز", "مراغه", "میانه", "مرند", "اهر"],
    "آذربایجان غربی": ["ارومیه", "خوی", "ماکو", "میاندوآب", "پیرانشهر"],
    "اردبیل": ["اردبیل", "مشگین‌شهر", "پارس‌آباد", "بیله‌سوار"],
    "اصفهان": ["اصفهان", "کاشان", "خمینی‌شهر", "نجف‌آباد", "شهرضا"],
    "البرز": ["کرج", "طالقان", "نظرآباد", "فردیس"],
    "ایلام": ["ایلام", "دهلران", "مهران", "ایوان"],
    "بوشهر": ["بوشهر", "دشتستان", "کنگان", "گناوه"],
    "تهران": ["تهران", "ری", "ورامین", "اسلامشهر", "دماوند"],
    "چهارمحال و بختیاری": ["شهرکرد", "بروجن", "فارسان", "لردگان"],
    "خراسان جنوبی": ["بیرجند", "قائن", "طبس", "فردوس"],
    "خراسان رضوی": ["مشهد", "سبزوار", "نیشابور", "تربت‌حیدریه"],
    "خراسان شمالی": ["بجنورد", "شیروان", "اسفراین", "مانه و سملقان"],
    "خوزستان": ["اهواز", "آبادان", "خرمشهر", "دزفول", "بهبهان"],
    "زنجان": ["زنجان", "ابهر", "خرمدره", "ماه‌نشان"],
    "سمنان": ["سمنان", "شاهرود", "دامغان", "گرمسار"],
    "سیستان و بلوچستان": ["زاهدان", "چابهار", "ایرانشهر", "زابل"],
    "فارس": ["شیراز", "مرودشت", "کازرون", "لار", "جهرم"],
    "قزوین": ["قزوین", "البرز", "تاکستان", "بوئین‌زهرا"],
    "قم": ["قم"],
    "کردستان": ["سنندج", "سقز", "بانه", "مریوان"],
    "کرمان": ["کرمان", "رفسنجان", "جیرفت", "سیرجان"],
    "کرمانشاه": ["کرمانشاه", "اسلام‌آباد غرب", "سرپل ذهاب", "پاوه"],
    "کهگیلویه و بویراحمد": ["یاسوج", "دهدشت", "گچساران"],
    "گلستان": ["گرگان", "گنبد کاووس", "علی‌آباد", "آق‌قلا"],
    "گیلان": ["رشت", "انزلی", "لاهیجان", "رودسر", "آستارا"],
    "لرستان": ["خرم‌آباد", "بروجرد", "الیگودرز", "دورود"],
    "مازندران": ["ساری", "آمل", "بابل", "بابلسر", "رامسر"],
    "مرکزی": ["اراک", "ساوه", "خمین", "محلات"],
    "هرمزگان": ["بندرعباس", "قشم", "کیش", "میناب", "بندر لنگه"],
    "همدان": ["همدان", "ملایر", "نهاوند", "تویسرکان"],
    "یزد": ["یزد", "میبد", "اردکان", "تفت"]
};


document.addEventListener('DOMContentLoaded', () => {
    const provinceSelect = document.getElementById('province');
    const citySelect = document.getElementById('city');

    // بارگذاری استان‌ها در لیست کشویی
    Object.keys(provincesAndCities).forEach(province => {
        const option = document.createElement('option');
        option.value = province;
        option.textContent = province;
        provinceSelect.appendChild(option);
    });

    // تغییر شهرها بر اساس انتخاب استان
    provinceSelect.addEventListener('change', () => {
        const selectedProvince = provinceSelect.value;

        // پاک کردن شهرهای قبلی
        citySelect.innerHTML = '';
        citySelect.disabled = true;

        if (selectedProvince && provincesAndCities[selectedProvince]) {
            provincesAndCities[selectedProvince].forEach(city => {
                const option = document.createElement('option');
                option.value = city;
                option.textContent = city;
                citySelect.appendChild(option);
            });

            citySelect.disabled = false;
        } else {
            const option = document.createElement('option');
            option.value = '';
            option.textContent = 'لطفاً ابتدا استان را انتخاب کنید';
            citySelect.appendChild(option);
        }
    });
});
