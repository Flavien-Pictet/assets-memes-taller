import json
import random
import os

# Define global CTA elements that will be used across all categories
global_cta = {
    "title": "TALLER APP",
    "subtitle": "DOWNLOAD LINK IN PROFILE",
    "features": [
        "Personalized height growth plan",
        "Track your progress daily",
        "AI-powered height optimization"
    ],
    "app_screenshots": [
        "app_main_screen.png",
        "app_tracker_screen.png",
        "app_profile_screen.png"
    ],
    "cta_texts": [
        "Join 100,000+ users growing taller with our app",
        "Unlock your maximum height potential today",
        "Start your height journey now",
        "Don't miss your growth window - download now",
        "Scientifically proven height optimization"
    ],
    "background": "cta_background.png"
}

# Définition de la structure des catégories
carousel_categories = [
    {
        "category": "Food",
        "hooks": [
            "Best foods to grow taller",
            "Foods that maximize height",
            "Top 5 height-boosting foods",
            "Eat this to grow taller",
            "Superfoods for height gain",
            "Foods that increase HGH naturally",
            "Foods to avoid for height growth",
            "Nutrients for maximum height",
            "Diet tips to grow taller",
            "The #1 food for height growth"
        ],
        "images": [
            "T-bone_steak.png",
            "Beef_liver.png",
            "Salmon.png",
            "Eggs.png",
            "Spinach.png",
            "Carrots.png",
            "Milk.png",
            "Chicken_breast.png",
            "Greek_yogurt.png",
            "Oatmeal.png"
        ],
        "backgrounds": [
            "food_bg_1.png",
            "food_bg_2.png",
            "food_bg_3.png",
            "food_bg_4.png",
            "food_bg_5.png"
        ],
        "app_screenshots": [
            "food_tracker_screen.png",
            "nutrition_calculator.png",
            "meal_planner_screen.png"
        ],
        "cta_texts": [
            "Track your growth-boosting nutrients daily",
            "Get personalized meal plans for maximum height",
            "Monitor your height progress with our advanced tracker",
            "Join 50,000+ users who grew taller with our app",
            "Unlock your full height potential today"
        ]
    },
    {
        "category": "Symptoms",
        "hooks": [
            "Signs you've reached max height",
            "Are you still growing?",
            "How to tell if growth plates closed",
            "Signs you'll grow taller later",
            "Warning signs of stunted growth",
            "Signs your bones are still growing",
            "How to know if you're done growing",
            "Signs you'll grow way taller",
            "Signs you are killing your height",
            "The ultimate growth potential test"
        ],
        "images": [
            "Xray_growth_plates.png",
            "Knee_pain.png",
            "Spinal_posture.png",
            "Foot_size_change.png",
            "Bone_scan.png",
            "Shoe_size_check.png",
            "Wrist_xray.png",
            "Height_chart.png",
            "Puberty_stages.png",
            "Hormone_levels.png"
        ],
        "backgrounds": [
            "symptoms_bg_1.png",
            "symptoms_bg_2.png",
            "symptoms_bg_3.png",
            "symptoms_bg_4.png",
            "symptoms_bg_5.png"
        ],
        "app_screenshots": [
            "growth_tracker_screen.png",
            "symptom_analyzer.png",
            "growth_prediction_tool.png"
        ],
        "cta_texts": [
            "Track your growth plate status with our advanced tools",
            "Get personalized growth predictions based on your symptoms",
            "Join 100,000+ users monitoring their height potential",
            "Don't miss your growth window - start tracking today",
            "Maximize your remaining growth potential now"
        ]
    },
    {
        "category": "Exercises",
        "hooks": [
            "Best exercises to grow taller",
            "Daily stretches for height gain",
            "Workouts that increase height",
            "The #1 stretch for height growth",
            "Science-backed height exercises",
            "Morning routine to grow taller",
            "Exercises that boost HGH",
            "Fix posture to look taller instantly",
            "Does hanging make you taller?",
            "Ways to grow taller from worst to best"
        ],
        "images": [
            "Hanging_bar.png",
            "Cobra_stretch.png",
            "Jump_rope.png",
            "Dead_hangs.png",
            "Yoga_pose.png",
            "Sprinting.png",
            "Jumping_drills.png",
            "Posture_corrector.png",
            "Resistance_bands.png",
            "Foam_roller.png"
        ],
        "backgrounds": [
            "exercise_bg_1.png",
            "exercise_bg_2.png",
            "exercise_bg_3.png",
            "exercise_bg_4.png",
            "exercise_bg_5.png"
        ],
        "app_screenshots": [
            "exercise_routine_screen.png",
            "height_workout_planner.png",
            "posture_analyzer_tool.png"
        ],
        "cta_texts": [
            "Get custom height-boosting workout plans",
            "Track your stretching routine for maximum results",
            "Join 75,000+ users who improved their height with our exercises",
            "Analyze your posture and unlock hidden inches",
            "Start your height-maximizing fitness journey today"
        ]
    },
    {
        "category": "Sleep",
        "hooks": [
            "How sleep affects your height",
            "Sleep habits to grow taller",
            "How to maximize growth during sleep",
            "Deep sleep and height growth",
            "Best sleep schedule for height",
            "Growth hormone and sleep basics",
            "Sleep mistakes stunting your growth",
            "Best sleeping position for height",
            "How much sleep to grow taller",
            "Unusual habits to grow taller"
        ],
        "images": [
            "Deep_sleep.png",
            "Growth_hormone_cycle.png",
            "Proper_pillow_position.png",
            "Mattress_posture.png",
            "Napping_tips.png",
            "Melatonin_effects.png",
            "Optimal_sleep_hours.png",
            "Blue_light_exposure.png",
            "Sleep_deprivation.png",
            "Circadian_rhythm.png"
        ],
        "backgrounds": [
            "sleep_bg_1.png",
            "sleep_bg_2.png",
            "sleep_bg_3.png",
            "sleep_bg_4.png",
            "sleep_bg_5.png"
        ],
        "app_screenshots": [
            "sleep_tracker_screen.png",
            "hgh_optimizer_tool.png",
            "sleep_quality_analyzer.png"
        ],
        "cta_texts": [
            "Optimize your sleep for maximum height growth",
            "Track your sleep cycles to boost HGH production",
            "Join 60,000+ users who improved their height while sleeping",
            "Unlock your growth potential with better sleep",
            "Start maximizing your nighttime growth hormone today"
        ]
    }
]

# Add negative hooks to each category and negative backgrounds
for category in carousel_categories:
    category["negative_hooks"] = [
        f"Foods that will kill your height",
        f"5 {category['category'].lower()} mistakes stunting your growth",
        f"{category['category']} habits destroying your height potential",
        f"Warning: {category['category'].lower()} traps stopping your growth",
        f"Avoid these {category['category'].lower()} height killers"
    ]
    
    category["negative_backgrounds"] = [
        "negative_bg_1.png",
        "negative_bg_2.png",
        "negative_bg_3.png",
        "negative_bg_4.png",
        "negative_bg_5.png"
    ]

# Add content descriptions for each image in all categories
image_content = {
    # Food category image content
    "T-bone_steak.png": {
        "title": "1. Protein-Rich Foods",
        "description": "High-quality protein supports bone and muscle development"
    },
    "Beef_liver.png": {
        "title": "2. Vitamin D Sources",
        "description": "Essential for calcium absorption and bone growth"
    },
    "Salmon.png": {
        "title": "3. Omega-3 Rich Fish",
        "description": "Promotes bone density and reduces inflammation"
    },
    "Eggs.png": {
        "title": "4. Complete Protein",
        "description": "Contains all essential amino acids for growth"
    },
    "Spinach.png": {
        "title": "5. Leafy Greens",
        "description": "Rich in calcium, magnesium and vitamin K"
    },
    "Carrots.png": {
        "title": "6. Vitamin A Foods",
        "description": "Supports bone cell growth and development"
    },
    "Milk.png": {
        "title": "7. Calcium Sources",
        "description": "The building block for stronger, taller bones"
    },
    "Chicken_breast.png": {
        "title": "8. Lean Protein",
        "description": "Fuels muscle growth without excess fat"
    },
    "Greek_yogurt.png": {
        "title": "9. Probiotic Foods",
        "description": "Improves nutrient absorption for growth"
    },
    "Oatmeal.png": {
        "title": "10. Complex Carbs",
        "description": "Sustained energy for growth and recovery"
    },
    
    # Symptoms category image content
    "Xray_growth_plates.png": {
        "title": "1. Growth Plate Status",
        "description": "Open plates mean height potential remains"
    },
    "Knee_pain.png": {
        "title": "2. Growing Pains",
        "description": "Common sign of active bone growth"
    },
    "Spinal_posture.png": {
        "title": "3. Posture Changes",
        "description": "Indicates ongoing spinal development"
    },
    "Foot_size_change.png": {
        "title": "4. Foot Growth",
        "description": "Often precedes height increase phases"
    },
    "Bone_scan.png": {
        "title": "5. Bone Density",
        "description": "Higher density supports vertical growth"
    },
    "Shoe_size_check.png": {
        "title": "6. Rapid Shoe Changes",
        "description": "Strong indicator of active growth"
    },
    "Wrist_xray.png": {
        "title": "7. Wrist Development",
        "description": "Reveals bone age and growth potential"
    },
    "Height_chart.png": {
        "title": "8. Growth Patterns",
        "description": "Track your height velocity curve"
    },
    "Puberty_stages.png": {
        "title": "9. Puberty Markers",
        "description": "Correlate with height growth phases"
    },
    "Hormone_levels.png": {
        "title": "10. Growth Hormone",
        "description": "Optimal levels maximize height potential"
    },
    
    # Exercises category image content
    "Hanging_bar.png": {
        "title": "1. Hanging Exercises",
        "description": "Decompresses spine and stretches muscles"
    },
    "Cobra_stretch.png": {
        "title": "2. Spinal Stretches",
        "description": "Improves posture and vertebral alignment"
    },
    "Jump_rope.png": {
        "title": "3. Impact Exercises",
        "description": "Stimulates bone growth through compression"
    },
    "Dead_hangs.png": {
        "title": "4. Passive Hanging",
        "description": "Lengthens spine and releases tension"
    },
    "Yoga_pose.png": {
        "title": "5. Yoga Positions",
        "description": "Enhances flexibility and spinal health"
    },
    "Sprinting.png": {
        "title": "6. Sprint Training",
        "description": "Triggers HGH release for growth"
    },
    "Jumping_drills.png": {
        "title": "7. Plyometrics",
        "description": "Strengthens growth plates and bones"
    },
    "Posture_corrector.png": {
        "title": "8. Posture Training",
        "description": "Instantly adds inches to your height"
    },
    "Resistance_bands.png": {
        "title": "9. Resistance Work",
        "description": "Builds supporting muscles for height"
    },
    "Foam_roller.png": {
        "title": "10. Myofascial Release",
        "description": "Improves alignment and reduces tension"
    },
    
    # Sleep category image content
    "Deep_sleep.png": {
        "title": "1. Deep Sleep Cycles",
        "description": "When 80% of growth hormone is released"
    },
    "Growth_hormone_cycle.png": {
        "title": "2. HGH Timing",
        "description": "Peaks during first 3 hours of sleep"
    },
    "Proper_pillow_position.png": {
        "title": "3. Spine Alignment",
        "description": "Proper support maximizes overnight growth"
    },
    "Mattress_posture.png": {
        "title": "4. Sleep Surface",
        "description": "Medium-firm support optimizes growth"
    },
    "Napping_tips.png": {
        "title": "5. Strategic Napping",
        "description": "Additional growth hormone release periods"
    },
    "Melatonin_effects.png": {
        "title": "6. Sleep Hormones",
        "description": "Regulate growth cycles and recovery"
    },
    "Optimal_sleep_hours.png": {
        "title": "7. Sleep Duration",
        "description": "8-10 hours maximizes growth potential"
    },
    "Blue_light_exposure.png": {
        "title": "8. Screen Effects",
        "description": "Disrupts growth hormone production"
    },
    "Sleep_deprivation.png": {
        "title": "9. Sleep Debt",
        "description": "Reduces height potential by 20-30%"
    },
    "Circadian_rhythm.png": {
        "title": "10. Sleep Timing",
        "description": "10pm-2am is prime growth window"
    }
}

# Modify the carousel generation to include image content
formatted_carousels = []

for category in carousel_categories:
    # Process positive hooks
    for hook_index, hook in enumerate(category["hooks"]):
        # Select 4 images for screens 2-5
        selected_images = category["images"][hook_index % len(category["images"]):hook_index % len(category["images"])+4]
        while len(selected_images) < 4:  # If we reach the end of the list, wrap around
            selected_images += category["images"][:4-len(selected_images)]
        
        # Select a background and app screenshot
        background = category["backgrounds"][hook_index % len(category["backgrounds"])]
        app_screenshot = global_cta["app_screenshots"][hook_index % len(global_cta["app_screenshots"])]
        cta_text = global_cta["cta_texts"][hook_index % len(global_cta["cta_texts"])]
        
        # Create the carousel structure
        carousel = {
            "category": category["category"],
            "screens": [
                {
                    "type": "hook",
                    "text": hook,
                    "background": background
                }
            ]
        }
        
        # Add 4 content screens with image content
        for i in range(4):
            img = selected_images[i]
            carousel["screens"].append({
                "type": "content",
                "title": image_content[img]["title"],
                "subtitle": image_content[img]["description"],
                "image": img
            })
        
        # Add CTA screen using global CTA
        carousel["screens"].append({
            "type": "cta",
            "title": global_cta["title"],
            "subtitle": global_cta["subtitle"],
            "features": global_cta["features"],
            "app_screenshot": app_screenshot,
            "cta_text": cta_text,
            "background": global_cta["background"]
        })
        
        formatted_carousels.append(carousel)

    # Process negative hooks
    for hook_index, hook in enumerate(category["negative_hooks"]):
        # Select 4 images for screens 2-5
        selected_images = category["images"][hook_index % len(category["images"]):hook_index % len(category["images"])+4]
        while len(selected_images) < 4:
            selected_images += category["images"][:4-len(selected_images)]
        
        # Select a negative background and app screenshot
        background = category["negative_backgrounds"][hook_index % len(category["negative_backgrounds"])]
        app_screenshot = category["app_screenshots"][hook_index % len(category["app_screenshots"])]
        cta_text = category["cta_texts"][hook_index % len(category["cta_texts"])]
        
        # Create the carousel structure with negative hook
        carousel = {
            "category": category["category"],
            "is_negative": True,  # Flag to indicate this is a negative hook
            "screens": [
                {
                    "type": "hook",
                    "text": hook,
                    "background": background
                }
            ]
        }
        
        # Add 4 content screens with image content - for negative hooks, use warning-style titles
        for i in range(4):
            img = selected_images[i]
            content = image_content[img]
            # Create negative versions of the titles
            negative_title = f"{i+1}. Avoid {content['title'].split('. ')[1]}"
            negative_subtitle = f"Can stunt growth if not addressed properly"
            
            carousel["screens"].append({
                "type": "content",
                "title": negative_title,
                "subtitle": negative_subtitle,
                "image": img
            })
        
        # Add CTA screen using global CTA
        carousel["screens"].append({
            "type": "cta",
            "title": global_cta["title"],
            "subtitle": "AVOID HEIGHT KILLERS",
            "features": global_cta["features"],
            "app_screenshot": app_screenshot,
            "cta_text": cta_text,
            "background": global_cta["background"]
        })
        
        formatted_carousels.append(carousel)

# Save the formatted carousels to JSON
with open("height_maxxing_carousels.json", "w") as file:
    json.dump(formatted_carousels, file, indent=4)

print("JSON file generated successfully!")

def add_variations(text, is_negative=False):
    # List of possible emojis
    if is_negative:
        emojis = ["⚠️", "❌", "🚫", "⛔", "🔴", "🛑", "⚡", "💀", "🚨", "😱"]
        prefixes = ["Warning: ", "Stop: ", "Avoid: ", "Danger: ", "Never: ", 
                   "Alert: ", "Caution: ", "Don't: ", "Beware: ", "Harmful: "]
    else:
        emojis = ["✨", "🔥", "💪", "📈", "🚀", "⚡", "🌟", "💯", "🔍", "👀"]
        prefixes = ["", "Revealed: ", "Secret: ", "Discover: ", "Breaking: ", "Proven: ", 
                   "Science Says: ", "Experts Agree: ", "Research Shows: ", "Fact: "]
    
    # Add emoji and prefix logic
    if random.random() > 0.5:
        text = random.choice(emojis) + " " + text
    else:
        text = text + " " + random.choice(emojis)
    
    if random.random() > 0.7:
        text = random.choice(prefixes) + text
        
    return text

# Define the data structure for height maxxing carousels
height_maxxing_data = {
    "carousels": [
        {
            "title": "5 Ways to Maximize Your Height Potential",
            "slides": [
                {
                    "type": "cover",
                    "title": "5 Ways to Maximize Your Height Potential",
                    "background": "backgrounds/sleep/sleep1.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "1. Optimize Your Sleep",
                    "content": "Growth hormone is primarily released during deep sleep. Aim for 8-10 hours of quality sleep each night to maximize your growth potential.",
                    "background": "backgrounds/sleep/sleep2.jpg",
                    "image": "content_images/sleep/sleep_chart.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "2. Nutrition Matters",
                    "content": "Ensure adequate protein, calcium, vitamin D, zinc, and other essential nutrients that support bone growth and development.",
                    "background": "backgrounds/food/food1.jpg",
                    "image": "content_images/food/nutrition_chart.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "3. Regular Exercise",
                    "content": "Weight-bearing exercises, stretching, and sports like basketball and swimming can help stimulate growth and improve posture.",
                    "background": "backgrounds/exercices/exercise1.jpg",
                    "image": "content_images/exercices/exercise_types.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "4. Maintain Good Posture",
                    "content": "Poor posture can make you appear shorter. Practice standing and sitting straight to maximize your current height.",
                    "background": "backgrounds/exercices/posture.jpg",
                    "image": "content_images/exercices/posture_comparison.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "5. Avoid Growth Inhibitors",
                    "content": "Minimize caffeine, alcohol, smoking, and stress as they can potentially interfere with growth during development years.",
                    "background": "backgrounds/negative/negative1.jpg",
                    "image": "content_images/symptoms/growth_inhibitors.jpg",
                    "text_color": "white"
                },
                {
                    "type": "cta",
                    "title": "Want More Height Maximizing Tips?",
                    "content": "Download our Height Maxxing Guide for a complete program to reach your full height potential!",
                    "background": "backgrounds/sleep/sleep3.jpg",
                    "cta_button": "Download Free Guide",
                    "cta_link": "https://heightmaxxing.com/guide",
                    "text_color": "white"
                }
            ]
        },
        {
            "title": "The Science of Height Growth",
            "slides": [
                {
                    "type": "cover",
                    "title": "The Science of Height Growth",
                    "background": "backgrounds/sleep/science.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "Growth Plate Fusion",
                    "content": "Height growth stops when growth plates fuse, typically between ages 14-19 for girls and 16-22 for boys.",
                    "background": "backgrounds/symptoms/growth_plates.jpg",
                    "image": "content_images/symptoms/growth_plate_diagram.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "Growth Hormone Cycle",
                    "content": "70% of growth hormone is released during deep sleep cycles, making quality sleep essential for height development.",
                    "background": "backgrounds/sleep/sleep_cycle.jpg",
                    "image": "content_images/sleep/hormone_cycle.jpg",
                    "text_color": "white"
                },
                {
                    "type": "content",
                    "title": "Nutrition & Growth",
                    "content": "Protein provides the building blocks for growth, while calcium and vitamin D are essential for bone development.",
                    "background": "backgrounds/food/nutrition_science.jpg",
                    "image": "content_images/food/nutrient_chart.jpg",
                    "text_color": "white"
                },
                {
                    "type": "cta",
                    "title": "Understand Your Growth Potential",
                    "content": "Get our free height assessment tool to understand your genetic potential and optimal growth window.",
                    "background": "backgrounds/sleep/potential.jpg",
                    "cta_button": "Get Free Assessment",
                    "cta_link": "https://heightmaxxing.com/assessment",
                    "text_color": "white"
                }
            ]
        }
    ]
}

def generate_data_file():
    """Generate the height_maxxing_carousels.json file if it doesn't exist"""
    file_path = "height_maxxing_carousels.json"
    
    if not os.path.exists(file_path):
        print(f"Creating data file: {file_path}")
        with open(file_path, 'w') as f:
            json.dump(height_maxxing_data, f, indent=4)
        print(f"Data file created successfully!")
    else:
        print(f"Data file already exists: {file_path}")

if __name__ == "__main__":
    generate_data_file()
