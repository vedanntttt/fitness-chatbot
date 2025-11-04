"""
Fallback exercise database for when API is unavailable
"""

EXERCISE_DATABASE = {
    "chest": [
        {
            "name": "Push-ups",
            "type": "strength",
            "muscle": "chest",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Start in a plank position with hands slightly wider than shoulders. Lower your body until chest nearly touches the floor, then push back up. Keep core tight throughout the movement."
        },
        {
            "name": "Incline Push-ups",
            "type": "strength", 
            "muscle": "chest",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Place hands on an elevated surface like a bench or step. Perform push-up motion, lowering chest toward the elevated surface. This variation is easier than standard push-ups."
        },
        {
            "name": "Chest Dips",
            "type": "strength",
            "muscle": "chest", 
            "equipment": "body_only",
            "difficulty": "intermediate",
            "instructions": "Using parallel bars or sturdy chairs, support your body weight on straight arms. Lower your body by bending arms until shoulders are below elbows, then push back up."
        },
        {
            "name": "Wide-Grip Push-ups",
            "type": "strength",
            "muscle": "chest",
            "equipment": "body_only", 
            "difficulty": "beginner",
            "instructions": "Similar to regular push-ups but with hands placed wider than shoulder-width. This targets the outer chest muscles more effectively."
        },
        {
            "name": "Diamond Push-ups",
            "type": "strength",
            "muscle": "chest",
            "equipment": "body_only",
            "difficulty": "advanced", 
            "instructions": "Form a diamond shape with your hands by touching thumbs and index fingers together. Perform push-ups in this position to target triceps and inner chest."
        }
    ],
    "biceps": [
        {
            "name": "Bicep Curls",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "dumbbells",
            "difficulty": "beginner",
            "instructions": "Stand with dumbbells at your sides, palms facing forward. Curl weights up toward shoulders, squeezing biceps at the top, then slowly lower back down."
        },
        {
            "name": "Hammer Curls",
            "type": "strength",
            "muscle": "biceps", 
            "equipment": "dumbbells",
            "difficulty": "beginner",
            "instructions": "Hold dumbbells with neutral grip (palms facing each other). Curl weights up toward shoulders while maintaining neutral grip throughout the movement."
        },
        {
            "name": "Chin-ups",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "pull_up_bar",
            "difficulty": "intermediate",
            "instructions": "Hang from pull-up bar with underhand grip, hands shoulder-width apart. Pull your body up until chin clears the bar, then lower with control."
        },
        {
            "name": "Resistance Band Curls",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "resistance_bands",
            "difficulty": "beginner", 
            "instructions": "Stand on resistance band with feet hip-width apart. Hold handles and curl up toward shoulders, maintaining tension throughout the movement."
        }
    ],
    "legs": [
        {
            "name": "Squats",
            "type": "strength",
            "muscle": "quadriceps",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Stand with feet shoulder-width apart. Lower your body by bending knees and hips as if sitting back into a chair. Keep chest up and knees behind toes."
        },
        {
            "name": "Lunges", 
            "type": "strength",
            "muscle": "quadriceps",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Step forward with one leg, lowering hips until both knees are bent at 90 degrees. Push back to starting position and repeat with other leg."
        },
        {
            "name": "Wall Sit",
            "type": "strength",
            "muscle": "quadriceps", 
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Lean back against wall with feet shoulder-width apart and about 2 feet from wall. Slide down until thighs are parallel to floor. Hold position."
        },
        {
            "name": "Calf Raises",
            "type": "strength",
            "muscle": "calves",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Stand with balls of feet on elevated surface, heels hanging off. Rise up on toes as high as possible, then slowly lower heels below the starting position."
        }
    ],
    "back": [
        {
            "name": "Pull-ups",
            "type": "strength", 
            "muscle": "lats",
            "equipment": "pull_up_bar",
            "difficulty": "intermediate",
            "instructions": "Hang from pull-up bar with overhand grip, hands wider than shoulders. Pull body up until chin clears bar, then lower with control."
        },
        {
            "name": "Superman",
            "type": "strength",
            "muscle": "lats",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Lie face down with arms extended overhead. Simultaneously lift chest, arms, and legs off the ground, holding briefly before lowering back down."
        },
        {
            "name": "Bird Dog",
            "type": "strength",
            "muscle": "lats",
            "equipment": "body_only", 
            "difficulty": "beginner",
            "instructions": "Start on hands and knees. Extend opposite arm and leg simultaneously, hold briefly, then return to start. Repeat with other arm and leg."
        }
    ],
    "abs": [
        {
            "name": "Plank",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Hold a push-up position with forearms on the ground. Keep body in straight line from head to heels, engaging core muscles throughout."
        },
        {
            "name": "Crunches",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "body_only",
            "difficulty": "beginner", 
            "instructions": "Lie on back with knees bent, hands behind head. Lift shoulders off ground by contracting abs, then slowly lower back down."
        },
        {
            "name": "Mountain Climbers",
            "type": "cardio",
            "muscle": "abdominals", 
            "equipment": "body_only",
            "difficulty": "intermediate",
            "instructions": "Start in plank position. Quickly alternate bringing knees toward chest in a running motion while maintaining plank position."
        },
        {
            "name": "Russian Twists",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "instructions": "Sit with knees bent, lean back slightly. Rotate torso left and right, touching ground beside hips with hands. Keep feet off ground for added difficulty."
        }
    ],
    "shoulders": [
        {
            "name": "Pike Push-ups",
            "type": "strength",
            "muscle": "shoulders",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "instructions": "Start in downward dog position. Lower head toward ground by bending arms, then push back up. This targets shoulder muscles effectively."
        },
        {
            "name": "Arm Circles", 
            "type": "strength",
            "muscle": "shoulders",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Extend arms out to sides parallel to ground. Make small circles forward for 30 seconds, then backward for 30 seconds. Gradually increase circle size."
        }
    ],
    "cardio": [
        {
            "name": "Jumping Jacks",
            "type": "cardio",
            "muscle": "full_body",
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Stand with feet together, arms at sides. Jump while spreading legs shoulder-width apart and raising arms overhead. Jump back to starting position."
        },
        {
            "name": "High Knees",
            "type": "cardio",
            "muscle": "full_body", 
            "equipment": "body_only",
            "difficulty": "beginner",
            "instructions": "Run in place, bringing knees up toward chest as high as possible. Pump arms naturally and maintain quick tempo."
        },
        {
            "name": "Burpees",
            "type": "cardio",
            "muscle": "full_body",
            "equipment": "body_only",
            "difficulty": "advanced",
            "instructions": "Start standing, drop into squat, kick feet back to plank, do push-up, jump feet back to squat, then jump up with arms overhead."
        }
    ]
}

def get_fallback_exercises(muscle_group: str = "", exercise_type: str = "", difficulty: str = "") -> list:
    """Get exercises from fallback database"""
    all_exercises = []
    
    # Collect exercises based on criteria
    if muscle_group:
        muscle_group = muscle_group.lower()
        # Handle common variations
        muscle_mapping = {
            'chest': 'chest',
            'arms': 'biceps', 
            'bicep': 'biceps',
            'triceps': 'biceps',  # We'll group arm exercises
            'legs': 'legs',
            'quads': 'legs',
            'quadriceps': 'legs',
            'glutes': 'legs',
            'back': 'back',
            'lats': 'back',
            'abs': 'abs',
            'core': 'abs',
            'abdominals': 'abs',
            'shoulders': 'shoulders',
            'cardio': 'cardio'
        }
        
        mapped_muscle = muscle_mapping.get(muscle_group, muscle_group)
        if mapped_muscle in EXERCISE_DATABASE:
            all_exercises = EXERCISE_DATABASE[mapped_muscle].copy()
    else:
        # If no muscle group specified, get from all categories
        for exercises in EXERCISE_DATABASE.values():
            all_exercises.extend(exercises)
    
    # Filter by type if specified
    if exercise_type:
        exercise_type = exercise_type.lower()
        all_exercises = [ex for ex in all_exercises if ex['type'].lower() == exercise_type]
    
    # Filter by difficulty if specified  
    if difficulty:
        difficulty = difficulty.lower()
        all_exercises = [ex for ex in all_exercises if ex['difficulty'].lower() == difficulty]
    
    # Return up to 5 exercises
    return all_exercises[:5] if all_exercises else []