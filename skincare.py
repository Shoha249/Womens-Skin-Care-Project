def get_skin_type():
    print("Please select your skin type:")
    print("1. Oily")
    print("2. Dry")
    print("3. Combination")
    skin_type = input("Enter your choice (1/2/3): ")
    return skin_type

def get_skin_condition():
    print("\nDo you have pimples or acne?")
    print("1. Yes")
    print("2. No")
    pimples = input("Enter your choice (1/2): ")
    return pimples

def get_age_group():
    print("\nPlease select your age group:")
    print("1. Below 20")
    print("2. 21-40")
    print("3. Above 40")
    age_group = input("Enter your choice (1/2/3): ")
    return age_group

def suggest_skincare(skin_type, pimples, age_group):
    print("\n--- Suggestions Based on Your Skin ---")
    
    if skin_type == '1':  # Oily
        print("🥰 Cleanse your face twice daily with a gentle face wash.")
        print("🥰 Use a light moisturizer to avoid clogging pores.")
        if pimples == '1':
            print("🥰 Use an anti-acne gel or a salicylic acid-based product.")
        print("🥰1" \
        " Try using a clay mask once a week.")
    elif skin_type == '2':  # Dry
        print("🥰 Use a hydrating face wash with no alcohol.")
        print("🥰 Use a rich, nourishing moisturizer.")
        if pimples == '1':
            print("🥰 Use a gentle acne treatment like benzoyl peroxide, but make sure it doesn't dry out your skin.")
        print("🥰 Use a hydrating mask once a week.")
    elif skin_type == '3':  # Combination
        print("🥰 Use a mild face wash to balance your skin.")
        print("🥰 Apply a lightweight moisturizer for T-zone and a richer one for dry areas.")
        if pimples == '1':
            print("🥰 Use an acne treatment gel on problem areas.")
        print("🥰 Use a mild exfoliator once a week.")
    
    print("\n--- Suggested Fruits for Skin ---")
    if age_group == '1':  # Below 20
        print("- Oranges (rich in Vitamin C for glow)")
        print("- Apples (help with skin hydration)")
        print("- Bananas (great for moisture)")
    elif age_group == '2':  # 21-40
        print("- Strawberries (packed with antioxidants)")
        print("- Papaya (helps with pigmentation)")
        print("- Mangoes (good for skin rejuvenation)")
    elif age_group == '3':  # Above 40
        print("- Blueberries (anti-aging and wrinkle prevention)")
        print("- Avocados (great for dry skin and wrinkles)")
        print("- Kiwi (rich in Vitamin C)")

    print("\n--- Suggested Exercises for Glowing Skin ---")
    if pimples == '1':
        print("- Try light yoga to reduce stress (stress can increase acne).")
    else:
        print("- Aerobic exercises like running or cycling to boost blood circulation.")
    print("- Regular stretching exercises for better posture and stress relief.")
    
def main():
    skin_type = get_skin_type()
    pimples = get_skin_condition()
    age_group = get_age_group()
    
    suggest_skincare(skin_type, pimples, age_group)
    
if __name__ == "__main__":
    main()
