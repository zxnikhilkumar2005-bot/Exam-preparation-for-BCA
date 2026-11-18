# Unit 14: Working with UI Controls

## Unit Overview
This unit covers CSS styling in JavaFX, FXML for UI definition, event handling in detail, and effects/animation/media in JavaFX.

---

## 14.1 CSS Styling in JavaFX

### CSS in JavaFX
- **Cascading Style Sheets** adapted for JavaFX
- Properties prefixed with `-fx-`
- Applied to scene or parent nodes
- Similar to web CSS but for JavaFX nodes

### Applying CSS

#### 1. Inline Style (Programmatic)
```java
Button btn = new Button("Styled");
btn.setStyle("-fx-background-color: blue; -fx-text-fill: white; -fx-font-size: 14px;");
```

#### 2. Style Class (Recommended)
```java
// In Java
Button btn = new Button("Styled");
btn.getStyleClass().add("my-button");

// In CSS file (style.css)
.my-button {
    -fx-background-color: blue;
    -fx-text-fill: white;
    -fx-font-size: 14px;
}

// Load CSS
scene.getStylesheets().add("style.css");
```

#### 3. ID Selector
```java
// In Java
Button btn = new Button("Styled");
btn.setId("submit-btn");

// In CSS
#submit-btn {
    -fx-background-color: green;
}
```

### CSS Syntax Rules
```css
/* Selector { property: value; } */

/* Type selector */
Button { -fx-background-color: gray; }

/* Class selector */
.my-class { -fx-background-color: blue; }

/* ID selector */
#my-id { -fx-background-color: red; }

/* Multiple properties */
.my-button {
    -fx-background-color: #3498db;
    -fx-text-fill: white;
    -fx-font-size: 14px;
    -fx-font-family: "Arial";
    -fx-padding: 10 20;
    -fx-border-radius: 5;
    -fx-background-radius: 5;
}
```

### Common JavaFX CSS Properties

| Property | Description | Example |
|----------|-------------|---------|
| `-fx-background-color` | Background color | `#3498db`, `red`, `rgba(0,0,0,0.5)` |
| `-fx-text-fill` | Text color | `white`, `#333` |
| `-fx-font-size` | Font size | `14px`, `1.2em` |
| `-fx-font-family` | Font family | `"Arial"`, `"Segoe UI"` |
| `-fx-font-weight` | Font weight | `bold`, `normal` |
| `-fx-padding` | Padding | `10px`, `10 20 10 20` |
| `-fx-margin` | Margin | `10px` |
| `-fx-border-color` | Border color | `black` |
| `-fx-border-width` | Border width | `2px` |
| `-fx-border-radius` | Border radius | `5px` |
| `-fx-background-radius` | Background radius | `5px` |
| `-fx-alignment` | Alignment | `center`, `top-left` |
| `-fx-spacing` | Spacing (layouts) | `10px` |
| `-fx-opacity` | Opacity | `0.5` (0-1) |
| `-fx-cursor` | Cursor type | `hand`, `crosshair` |

### Pseudo-classes
```css
/* Hover state */
.my-button:hover {
    -fx-background-color: #2980b9;
}

/* Pressed state */
.my-button:pressed {
    -fx-background-color: #1c6ea4;
}

/* Focused state */
.my-button:focused {
    -fx-border-color: #3498db;
    -fx-border-width: 2px;
}

/* Disabled state */
.my-button:disabled {
    -fx-opacity: 0.5;
}
```

### Complete CSS Example

**style.css:**
```css
.root {
    -fx-background-color: #f0f0f0;
    -fx-font-family: "Segoe UI", "Arial";
    -fx-font-size: 14px;
}

.label {
    -fx-text-fill: #2c3e50;
    -fx-font-weight: bold;
}

.text-field {
    -fx-background-color: white;
    -fx-border-color: #bdc3c7;
    -fx-border-radius: 4;
    -fx-padding: 8;
}

.text-field:focused {
    -fx-border-color: #3498db;
    -fx-effect: dropshadow(gaussian, #3498db, 5, 0, 0, 0);
}

.button {
    -fx-background-color: #3498db;
    -fx-text-fill: white;
    -fx-padding: 10 20;
    -fx-border-radius: 4;
    -fx-cursor: hand;
}

.button:hover {
    -fx-background-color: #2980b9;
}

.button:pressed {
    -fx-background-color: #1c6ea4;
}

.button.cancel {
    -fx-background-color: #e74c3c;
}

.button.cancel:hover {
    -fx-background-color: #c0392b;
}
```

**Java Code:**
```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.geometry.*;

public class CSSExample extends Application {
    @Override
    public void start(Stage stage) {
        Label label = new Label("Login Form");
        label.getStyleClass().add("label");
        
        TextField username = new TextField();
        username.setPromptText("Username");
        username.getStyleClass().add("text-field");
        
        PasswordField password = new PasswordField();
        password.setPromptText("Password");
        password.getStyleClass().add("text-field");
        
        Button loginBtn = new Button("Login");
        loginBtn.getStyleClass().add("button");
        
        Button cancelBtn = new Button("Cancel");
        cancelBtn.getStyleClass().addAll("button", "cancel");
        
        VBox root = new VBox(15, label, username, password, loginBtn, cancelBtn);
        root.setAlignment(Pos.CENTER);
        root.setPadding(new Insets(30));
        root.getStyleClass().add("root");
        
        Scene scene = new Scene(root, 400, 400);
        scene.getStylesheets().add("style.css");
        
        stage.setTitle("CSS Styled Form");
        stage.setScene(scene);
        stage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

## 14.2 FXML (JavaFX Markup Language)

### What is FXML?
- **XML-based** declarative language for defining JavaFX UI
- Separates **View** (FXML) from **Controller** (Java logic)
- Used with **Scene Builder** (visual editor)

### FXML Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.scene.layout.*?>
<?import javafx.scene.control.*?>
<?import javafx.geometry.*?>

<VBox xmlns:fx="http://javafx.com/fxml/1" 
      fx:controller="com.example.LoginController"
      spacing="15" alignment="CENTER" prefWidth="400" prefHeight="400">
    <padding>
        <Insets top="30" right="30" bottom="30" left="30"/>
    </padding>
    
    <Label text="Login Form" styleClass="label"/>
    
    <TextField fx:id="usernameField" promptText="Username" styleClass="text-field"/>
    <PasswordField fx:id="passwordField" promptText="Password" styleClass="text-field"/>
    
    <HBox spacing="10" alignment="CENTER">
        <Button text="Login" fx:id="loginBtn" styleClass="button" onAction="#handleLogin"/>
        <Button text="Cancel" fx:id="cancelBtn" styleClass="button cancel" onAction="#handleCancel"/>
    </HBox>
</VBox>
```

### Key FXML Attributes

| Attribute | Purpose |
|-----------|---------|
| `fx:id` | Unique identifier; injected into controller |
| `fx:controller` | Fully qualified controller class name |
| `onAction="#method"` | Event handler method in controller |
| `styleClass` | CSS class names (space-separated) |
| `style` | Inline CSS |

### Controller Class
```java
package com.example;

import javafx.fxml.FXML;
import javafx.scene.control.*;

public class LoginController {
    @FXML private TextField usernameField;
    @FXML private PasswordField passwordField;
    @FXML private Button loginBtn;
    @FXML private Button cancelBtn;
    
    @FXML
    public void initialize() {
        // Called after FXML loaded
        loginBtn.setDefaultButton(true);
    }
    
    @FXML
    private void handleLogin() {
        String user = usernameField.getText();
        String pass = passwordField.getText();
        
        if ("admin".equals(user) && "1234".equals(pass)) {
            System.out.println("Login successful!");
        } else {
            System.out.println("Invalid credentials");
        }
    }
    
    @FXML
    private void handleCancel() {
        usernameField.clear();
        passwordField.clear();
    }
}
```

### Loading FXML
```java
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("login.fxml"));
        Parent root = loader.load();
        
        Scene scene = new Scene(root);
        scene.getStylesheets().add("style.css");
        
        stage.setTitle("FXML Login");
        stage.setScene(scene);
        stage.show();
    }
}
```

---

## 14.3 Event Handling in Detail

### Event Hierarchy
```
EventObject (java.util)
    │
    └─ Event (javafx.event)
         │
         ├─ ActionEvent
         ├─ InputEvent
         │    │
         │    ├─ MouseEvent
         │    ├─ KeyEvent
         │    ├─ TouchEvent
         │    └─ DragEvent
         ├─ WindowEvent
         └─ ...
```

### Event Handling Approaches

#### 1. Lambda Expression (Java 8+)
```java
// ActionEvent (Button click)
button.setOnAction(e -> System.out.println("Clicked!"));

// MouseEvent
node.setOnMouseClicked(e -> {
    System.out.println("Clicked at: " + e.getX() + ", " + e.getY());
});

// KeyEvent
textField.setOnKeyPressed(e -> {
    if (e.getCode() == KeyCode.ENTER) {
        System.out.println("Enter pressed");
    }
});
```

#### 2. EventHandler Interface
```java
button.setOnAction(new EventHandler<ActionEvent>() {
    @Override
    public void handle(ActionEvent event) {
        System.out.println("Button clicked!");
    }
});
```

#### 3. FXML Controller (Recommended for FXML)
```java
@FXML
private void handleButtonClick(ActionEvent event) {
    System.out.println("Clicked from FXML");
}
```

### Event Phases
```
1. ROUTE CONSTRUCTION
   Build path from source to root

2. CAPTURING PHASE
   Root → ... → Parent → Target
   (EventCaptureHandler)

3. TARGET PHASE
   At target node
   (EventHandler)

4. BUBBLING PHASE
   Target → Parent → ... → Root
   (EventHandler)
```

### Consuming Events
```java
// Prevent further propagation
event.consume();

// Check if consumed
if (event.isConsumed()) { ... }
```

### Event Filters (Capturing Phase)
```java
// Add filter for capturing phase
node.addEventFilter(KeyEvent.KEY_PRESSED, e -> {
    if (e.getCode() == KeyCode.ESCAPE) {
        e.consume();  // Prevent ESC key processing
    }
});
```

### Common Event Types

| Event | Source | Common Use |
|-------|--------|------------|
| `ActionEvent` | Button, MenuItem, Hyperlink | Click actions |
| `MouseEvent` | Any Node | Click, hover, drag |
| `KeyEvent` | TextField, TextArea, Scene | Keyboard input |
| `DragEvent` | Any Node | Drag & drop |
| `ScrollEvent` | ScrollPane, ListView | Mouse wheel |
| `WindowEvent` | Stage | Show, hide, close |

---

## 14.4 Effects, Animation and Media

### Visual Effects (javafx.scene.effect)

#### Common Effects
```java
import javafx.scene.effect.*;

// Drop Shadow
DropShadow shadow = new DropShadow();
shadow.setOffsetX(3);
shadow.setOffsetY(3);
shadow.setRadius(5);
shadow.setColor(Color.GRAY);
node.setEffect(shadow);

// Glow
Glow glow = new Glow(0.8);  // 0.0 to 1.0
node.setEffect(glow);

// Reflection
Reflection reflection = new Reflection();
reflection.setFraction(0.7);
reflection.setTopOpacity(0.5);
reflection.setBottomOpacity(0.1);
node.setEffect(reflection);

// Blur
GaussianBlur blur = new GaussianBlur(5);  // radius
node.setEffect(blur);

// Color Adjust
ColorAdjust adjust = new ColorAdjust();
adjust.setBrightness(0.2);
adjust.setContrast(0.5);
adjust.setSaturation(1.5);
node.setEffect(adjust);

// Blend (combine effects)
Blend blend = new Blend();
blend.setMode(BlendMode.MULTIPLY);
blend.setBottomInput(new ColorInput(0, 0, 100, 100, Color.RED));
blend.setTopInput(shadow);
node.setEffect(blend);
```

#### Chaining Effects
```java
// Apply multiple effects
EffectChain chain = new EffectChain();
chain.addEffect(new DropShadow());
chain.addEffect(new Glow(0.5));
node.setEffect(chain);
```

---

### Animation (javafx.animation)

#### Timeline (Keyframe Animation)
```java
import javafx.animation.*;
import javafx.util.Duration;

Timeline timeline = new Timeline(
    new KeyFrame(Duration.ZERO, 
        new KeyValue(node.translateXProperty(), 0)),
    new KeyFrame(Duration.seconds(2), 
        new KeyValue(node.translateXProperty(), 200)),
    new KeyFrame(Duration.seconds(4), 
        new KeyValue(node.translateXProperty(), 0))
);
timeline.setCycleCount(Animation.INDEFINITE);
timeline.setAutoReverse(true);
timeline.play();
```

#### Transitions (Pre-built Animations)

```java
// TranslateTransition (Move)
TranslateTransition tt = new TranslateTransition(Duration.seconds(2), node);
tt.setFromX(0); tt.setToX(200);
tt.setCycleCount(2);
tt.setAutoReverse(true);
tt.play();

// RotateTransition
RotateTransition rt = new RotateTransition(Duration.seconds(1), node);
rt.setByAngle(360);
rt.setCycleCount(Animation.INDEFINITE);
rt.play();

// ScaleTransition
ScaleTransition st = new ScaleTransition(Duration.seconds(1), node);
st.setFromX(1); st.setToX(2);
st.setFromY(1); st.setToY(2);
st.play();

// FadeTransition
FadeTransition ft = new FadeTransition(Duration.seconds(1), node);
ft.setFromValue(1.0); ft.setToValue(0.0);
ft.play();

// ParallelTransition (run together)
ParallelTransition pt = new ParallelTransition(node, tt, rt, ft);
pt.play();

// SequentialTransition (run in sequence)
SequentialTransition st2 = new SequentialTransition(node, ft, tt, rt);
st2.play();

// PauseTransition
PauseTransition pause = new PauseTransition(Duration.seconds(1));
pause.setOnFinished(e -> System.out.println("Paused done"));
pause.play();
```

#### Animation Control
```java
Animation anim = new TranslateTransition(...);

anim.play();           // Start
anim.pause();          // Pause
anim.stop();           // Stop (reset)
anim.setRate(2.0);     // Double speed
anim.setDelay(Duration.seconds(1));  // Delay start
anim.setCycleCount(5); // Repeat 5 times
anim.setAutoReverse(true);  // Reverse on alternate cycles

// Event handlers
anim.setOnFinished(e -> System.out.println("Animation done"));
anim.setOnPaused(e -> System.out.println("Paused"));
```

---

### Media (javafx.scene.media)

#### Audio Playback
```java
import javafx.scene.media.*;

// From file
Media media = new Media(new File("music.mp3").toURI().toString());
MediaPlayer player = new MediaPlayer(media);
player.play();

// Control
player.pause();
player.stop();
player.setVolume(0.5);  // 0.0 to 1.0
player.setMute(false);
player.setRate(1.0);    // Playback speed

// Events
player.setOnReady(() -> System.out.println("Ready"));
player.setOnEndOfMedia(() -> System.out.println("Finished"));
player.setOnError(() -> System.out.println("Error: " + player.getError()));
```

#### Video Playback
```java
// MediaView for video display
Media videoMedia = new Media(new File("video.mp4").toURI().toString());
MediaPlayer videoPlayer = new MediaPlayer(videoMedia);
MediaView mediaView = new MediaView(videoPlayer);

// Add to scene
root.getChildren().add(mediaView);

videoPlayer.play();

// Full screen
mediaView.setFitWidth(800);
mediaView.setFitHeight(600);
mediaView.setPreserveRatio(true);
```

#### Media Controls
```java
// Built-in controls (JavaFX 8+)
MediaControl control = new MediaControl(mediaPlayer);
// Or use MediaPlayer directly with custom UI

// Progress
videoPlayer.currentTimeProperty().addListener((obs, old, newVal) -> {
    double progress = newVal.toMillis() / videoPlayer.getTotalDuration().toMillis();
    progressBar.setProgress(progress);
});

// Seek
videoPlayer.seek(Duration.seconds(30));
```

---

## 14.5 Important Exam Questions (from PYQ Analysis)

### High Priority

**2-Mark Questions:**
1. How to apply CSS in JavaFX? (Inline, StyleClass, ID)
2. What is FXML? Key attributes (fx:id, fx:controller, onAction).
3. What is Scene Builder?
4. Event handling approaches in JavaFX.
5. Common JavaFX effects.
5. Difference between Timeline and Transitions.
6. How to play audio/video in JavaFX?

**5-Mark Questions:**
1. Explain CSS styling in JavaFX with example.
2. Explain FXML structure and controller with example.
3. Explain event handling in JavaFX (lambda, EventHandler, FXML).
4. Explain JavaFX effects with examples.
5. Explain animation: Timeline and Transitions.
6. Write program: MediaPlayer for audio/video.

**10-Mark Questions:**
1. **CSS, FXML, Event Handling, Effects, Animation, Media in JavaFX.** (Appeared 2024, 2025, 2026)
2. Complete JavaFX app with FXML, CSS, event handling, animation.

### Programs to Practice
1. ✅ **CSS styled form (style.css + Java)** - appeared 2024, 2025
2. ✅ **FXML login form with controller** - appeared 2024, 2025, 2026
3. ✅ **Event handling (Button click → Label update)** - appeared 2022, 2023, 2024, 2025, 2026
4. ✅ **Effects (DropShadow, Glow, Reflection)** - appeared 2025
5. ✅ **Animation (TranslateTransition, FadeTransition)** - appeared 2025
6. ✅ **MediaPlayer (audio/video)** - appeared 2025

---

## 14.6 Summary of Unit 14

| Topic | Key Points |
|-------|------------|
| **CSS** | `-fx-` prefix; inline, styleClass, ID; pseudo-classes (:hover, :pressed) |
| **FXML** | XML for UI; `fx:id`, `fx:controller`, `onAction`; Scene Builder |
| **Controller** | `@FXML` injection; `initialize()`; event handlers |
| **Event Handling** | Lambda (preferred), EventHandler, FXML `onAction`; filters vs handlers |
| **Effects** | DropShadow, Glow, Reflection, Blur, ColorAdjust, Blend |
| **Animation** | Timeline (KeyFrames), Transitions (Translate, Rotate, Scale, Fade) |
| **Parallel/Sequential** | Run animations together or in sequence |
| **Media** | Media, MediaPlayer, MediaView; audio/video; controls |
| **Integration** | FXML + CSS + Controller = MVC pattern |

---

## 14.7 Quick Reference: JavaFX CSS Properties

```css
/* Colors */
-fx-background-color: #3498db;
-fx-text-fill: white;
-fx-border-color: #2c3e50;

/* Fonts */
-fx-font-size: 14px;
-fx-font-family: "Segoe UI";
-fx-font-weight: bold;

/* Layout */
-fx-padding: 10 20;
-fx-spacing: 10;
-fx-alignment: center;

/* Borders */
-fx-border-width: 2px;
-fx-border-radius: 5;
-fx-background-radius: 5;

/* Effects */
-fx-opacity: 0.8;
-fx-effect: dropshadow(gaussian, gray, 5, 0, 2, 2);

/* States */
.button:hover { -fx-background-color: #2980b9; }
.button:pressed { -fx-background-color: #1c6ea4; }
.text-field:focused { -fx-border-color: #3498db; }
```