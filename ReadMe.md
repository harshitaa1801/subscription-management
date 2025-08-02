# DoReMi Subscription Management

## 📖 Context
DoReMi is a streaming app that allows users to:
- Listen to **music**
- Listen to **podcasts**
- Watch **videos**

They offer different subscription plans for each category of services.  
Users can subscribe to **one plan per category**.

**Default Rules:**
- Only **one device** streaming per plan by default.
- **One plan per category** at a time.

---

## 💳 Subscription Plans

### 🎵 Music Streaming
| Plan     | Details               | Price                |
|----------|-----------------------|----------------------|
| FREE     | 1 month trial         | ₹0                   |
| PERSONAL | 1 month               | ₹100                 |
| PREMIUM  | 3 months              | ₹250                 |

### 📺 Video Streaming
| Plan     | Details               | Price                |
|----------|-----------------------|----------------------|
| FREE     | 1 month trial         | ₹0                   |
| PERSONAL | 1 month               | ₹200                 |
| PREMIUM  | 3 months              | ₹500                 |

### 🎙️ Podcast Streaming
| Plan     | Details               | Price                |
|----------|-----------------------|----------------------|
| FREE     | 1 month trial         | ₹0                   |
| PERSONAL | 1 month               | ₹100                 |
| PREMIUM  | 3 months              | ₹300                 |

---

## ➕ Top-Up Plans
Top-ups allow users to increase the number of devices they can stream to.

**Rules:**
- Only **one top-up** can be selected.
- The top-up applies to **all subscriptions**.
- A top-up can **only** be added if a subscription exists.

| Top-Up      | Devices      | Price                |
|-------------|-------------|----------------------|
| FOUR_DEVICE | Up to 4     | ₹50 for 1 month      |
| TEN_DEVICE  | Up to 10    | ₹100 for 1 month     |

---

## 🔔 Renewal Reminder
- Users must be **notified 10 days before** the plan expires.

---

## 🎯 Goal
Given a **subscription start date**, your program should:
1. **Print** the date when the reminder should be sent for each subscription category.
2. **Calculate** the total renewal amount:  
   - Sum of all subscription plan amounts  
   - Plus the top-up amount (if any)

---

## 📌 Assumptions
- A user can buy only **one plan per category** at a time.
- All plans default to **one device**.
- A user can buy only **one top-up** at a time.
- One top-up applies to **all active subscriptions**.

---
