# ট্র্যাপিজয়েডাল রুল ইমপ্লিমেন্টেশন

এই প্রজেক্টে Python এবং NumPy ব্যবহার করে ট্র্যাপিজয়েডাল রুলের বিভিন্ন দিক বাস্তবায়ন করা হয়েছে।

## প্রয়োজনীয় প্যাকেজ

- Python 3.7+
- NumPy
- Matplotlib

## ইনস্টলেশন

1. প্রথমে প্রয়োজনীয় প্যাকেজগুলো ইনস্টল করুন:
```bash
pip install -r requirements.txt
```

## ফাইল স্ট্রাকচার

1. **basic_trapezoidal_rule.py**
   - বেসিক ট্র্যাপিজয়েডাল রুল ইমপ্লিমেন্টেশন
   - চালানোর জন্য: `python basic_trapezoidal_rule.py`

2. **table_data_trapezoidal.py**
   - টেবিল ডাটা দিয়ে ট্র্যাপিজয়েডাল রুল
   - চালানোর জন্য: `python table_data_trapezoidal.py`

3. **multiple_intervals_trapezoidal.py**
   - বড় সংখ্যক ইন্টারভাল ব্যবহার করে ট্র্যাপিজয়েডাল রুল
   - চালানোর জন্য: `python multiple_intervals_trapezoidal.py`

4. **exact_comparison_trapezoidal.py**
   - এক্সাক্ট ইন্টিগ্রালের সাথে তুলনা
   - চালানোর জন্য: `python exact_comparison_trapezoidal.py`

5. **visualization_trapezoidal.py**
   - ফাংশন এবং ট্র্যাপিজয়েড ভিজুয়ালাইজেশন
   - চালানোর জন্য: `python visualization_trapezoidal.py`

6. **unequal_intervals_trapezoidal.py**
   - আনইকুয়াল ইন্টারভালের জন্য ট্র্যাপিজয়েডাল রুল
   - চালানোর জন্য: `python unequal_intervals_trapezoidal.py`

## ব্যবহার উদাহরণ

প্রতিটি ফাইলে `if __name__ == "__main__":` ব্লকে উদাহরণ দেওয়া আছে। আপনি চাইলে নিজের ফাংশন দিয়েও টেস্ট করতে পারেন।

উদাহরণস্বরূপ:
```python
from basic_trapezoidal_rule import basic_trapezoidal_rule

def my_function(x):
    return np.sin(x) * np.exp(-x)

result = basic_trapezoidal_rule(my_function, 0, np.pi, 100)
print(f"Result: {result}")
```

## নোট

- সব ফাংশনে টাইপ হিন্টিং ব্যবহার করা হয়েছে
- প্রতিটি ফাংশনে ডকুমেন্টেশন আছে
- এরর হ্যান্ডলিং এবং ইনপুট ভ্যালিডেশন করা আছে 