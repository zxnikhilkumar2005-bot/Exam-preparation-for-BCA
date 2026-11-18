# Unit 14: Working with UI Controls

## Unit Overview
This unit covers **JavaFX Architecture**, **CSS styling**, **FXML for UI definition**, **Event Handling** in detail, **Layout Panes**, **UI Controls**, and **Effects/Animation/Media** in JavaFX.

> **Exam Priority (PYQ Analysis 2021-2026):** 🔴 **CRITICAL** — JavaFX appears 6/10 years (2021–2026). Event Handling = 5/10 years (often 10 marks). JavaFX Features/Components/Layouts = 5-mark short note (2024, 2025×2, 2026). FXML+Controller = 5 marks (2024). Effects/Animation/Media = Low (2025 only).

---

## 14.0 JavaFX Architecture & Core Concepts (NEW — High Exam Priority)

> **PYQ:** 2021 Q5(a) 10m "JavaFX features", 2023 Q3(a) 10m "Swing vs AWT + JavaFX features", 2024 Q4(b) 10m "Event handling", 2025 Q1(h) 5m "AWT & Swing features", 2026 Q1(g) 5m "JavaFX features + components + layouts"

### JavaFX Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    JavaFX Application                       │
├─────────────────────────────────────────────────────────────┤
│  Scene Graph (Node hierarchy: Root → Parent → Children)    │
├─────────────────────────────────────────────────────────────┤
│  Pulse (Rendering Loop @ 60fps) → Prism (Graphics Pipeline)│
├─────────────────────────────────────────────────────────────┤
│  Glass (Windowing) + Media Engine + Web Engine             │
└─────────────────────────────────────────────────────────────┘
```

### Key Components
| Component | Description |
|-----------|-------------|
| **Stage** | Top-level container (window); contains a Scene |
| **Scene** | Container for all content (Scene Graph root) |
| **Scene Graph** | Hierarchical tree of Nodes (UI controls, layouts, shapes) |
| **Node** | Base class: `Parent` (containers), `Control` (UI controls), `Shape`, `MediaView` |
| **Prism** | Hardware-accelerated rendering pipeline |
| **Glass** | Platform-specific windowing layer |

### JavaFX vs AWT vs Swing
| Feature | AWT | Swing | JavaFX |
|---------|-----|-------|--------|
| **Release** | JDK 1.0 | JDK 1.2 | Java 8+ (separate module JDK 11+) |
| **Components** | Heavyweight (OS peers) | Lightweight (emulated) | **Lightweight + GPU-accelerated** |
| **Rendering** | OS-dependent | Java2D (CPU) | **Prism (GPU)** |
| **UI Definition** | Java code | Java code | **FXML (XML) + CSS + Java** |
| **MVC Support** | No | Partial | **Full (FXML=View, Controller=Logic)** |
| **CSS Styling** | No | Limited (UIManager) | **Full CSS3-like (-fx- prefix)** |
| **Animation** | Basic Timer | Timer-based | **Timeline, Transitions, Interpolation** |
| **Media** | No | Java Media Framework | **Built-in (Media, MediaPlayer, MediaView)** |
| **Web Content** | No | JEditorPane | **WebView (WebKit)** |
| **3D Support** | No | No | **Yes (Shape3D, Camera, Light)** |
| **Scene Builder** | No | No | **Visual drag-drop FXML editor** |

### JavaFX Application Lifecycle
```java
import javafx.application.Application;
import javafx.stage.Stage;

public class MyApp extends Application {
    @Override
    public void init() { /* Called before start() */ }
    
    @Override
    public void start(Stage primaryStage) { /* UI setup */ }
    
    @Override
    public void stop() { /* Cleanup on close */ }
    
    public static void main(String[] args) { launch(args); }
}
```

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

## 14.2 Layout Panes (Critical — "Components + Layouts" asked in 2026 Q1(g) 5m)

> **PYQ:** 2026 Q1(g) explicitly asks for "JavaFX features + components + layouts"

### Layout Hierarchy
```
Pane (abstract)
├── Region (resizable, CSS-stylable)
│   ├── BorderPane
│   ├── StackPane
│   ├── GridPane
│   ├── FlowPane
│   ├── TilePane
│   ├── AnchorPane
│   └── ...
├── HBox / VBox (simplest linear layouts)
└── Custom Pane
```

### Layout Comparison Table

| Layout | Arrangement | Best For | Key Properties |
|--------|-------------|----------|----------------|
| **HBox** | Horizontal row | Toolbars, button groups | `spacing`, `alignment`, `fillHeight` |
| **VBox** | Vertical column | Forms, stacked content | `spacing`, `alignment`, `fillWidth` |
| **BorderPane** | 5 regions (top, bottom, left, right, center) | Main app window structure | `setTop()`, `setCenter()`, etc. |
| **GridPane** | Grid (rows × columns) | Forms, calculators, data grids | `add(node, col, row)`, `Hgap`, `Vgap`, `columnConstraints` |
| **FlowPane** | Flow wrapping (horizontal/vertical) | Tag clouds, responsive galleries | `orientation`, `hgap`, `vgap`, `prefWrapLength` |
| **StackPane** | Stacked (centered, back-to-front) | Overlays, backgrounds, loading spinners | `alignment` (default CENTER) |
| **TilePane** | Uniform-sized tiles | Image galleries, icon grids | `prefColumns`, `prefRows`, `tileAlignment` |
| **AnchorPane** | Anchor to edges | Absolute positioning, resizing behavior | `setTopAnchor()`, `setLeftAnchor()`, etc. |

### Code Examples

**VBox (Form Layout)**
```java
VBox form = new VBox(15);                    // 15px spacing
form.setAlignment(Pos.CENTER);               // Center horizontally
form.setPadding(new Insets(20));             // Padding around edges
form.setFillWidth(true);                     // Children fill width
form.getChildren().addAll(label, textField, button);
```

**GridPane (Calculator/Grid Form)**
```java
GridPane grid = new GridPane();
grid.setHgap(10); grid.setVgap(10);
grid.setPadding(new Insets(20));
grid.setAlignment(Pos.CENTER);

// Add to specific cell
grid.add(new Label("Username:"), 0, 0);
grid.add(usernameField, 1, 0);
grid.add(new Label("Password:"), 0, 1);
grid.add(passwordField, 1, 1);

// Span columns
Button loginBtn = new Button("Login");
GridPane.setColumnSpan(loginBtn, 2);
grid.add(loginBtn, 0, 2);
```

**BorderPane (Main Window)**
```java
BorderPane root = new BorderPane();
root.setTop(menuBar);
root.setLeft(sideNav);
root.setCenter(contentArea);
root.setRight(inspector);
root.setBottom(statusBar);

// Region-only centers resize; others use preferred size
```

**HBox + VBox Nesting (Complex Forms)**
```java
VBox root = new VBox(20);
HBox buttonRow = new HBox(10, saveBtn, cancelBtn, deleteBtn);
buttonRow.setAlignment(Pos.CENTER_RIGHT);
root.getChildren().addAll(formFields, buttonRow);
```

---

## 14.3 UI Controls (The Unit's Core Topic)

> **PYQ:** GUI programs (name/email + button) appeared 2022, 2025. Event handling on controls = 5-10 marks.

### Control Hierarchy
```
Control (abstract)
├── Labeled (text + graphic)
│   ├── Label
│   ├── Button
│   │   ├── DefaultButton (Enter key)
│   │   └── CancelButton (ESC key)
│   ├── ToggleButton
│   │   ├── RadioButton (mutually exclusive in ToggleGroup)
│   │   └── CheckBox
│   ├── Hyperlink
│   └── MenuItem → Menu, CheckMenuItem, RadioMenuItem
├── TextInputControl
│   ├── TextField (single line)
│   ├── PasswordField (masked)
│   └── TextArea (multi-line)
├── ComboBox<T> / ChoiceBox<T>
├── ListView<T> / TableView<T> / TreeView<T>
├── Slider / ProgressBar / ProgressIndicator
├── ColorPicker / DatePicker
├── ToolBar / TabPane / Accordion / SplitPane
└── ScrollPane / Pagination
```

### Essential Controls with Code

| Control | Key Methods | Common Events |
|---------|-------------|---------------|
| **Button** | `setDefaultButton()`, `setCancelButton()`, `setOnAction()` | `ActionEvent` |
| **Label** | `setText()`, `setGraphic()`, `setTextAlignment()` | — |
| **TextField** | `getText()`, `setPromptText()`, `setPrefColumnCount()` | `ActionEvent` (Enter), `KeyEvent` |
| **PasswordField** | `getText()`, `setPromptText()` | `ActionEvent` |
| **TextArea** | `getText()`, `setWrapText(true)`, `setPrefRowCount()` | `KeyEvent` |
| **CheckBox** | `isSelected()`, `setSelected()`, `setIndeterminate()` | `ActionEvent` |
| **RadioButton** | `setToggleGroup()`, `isSelected()` | `ActionEvent` |
| **ComboBox** | `getItems()`, `getValue()`, `setOnAction()` | `ActionEvent` |
| **ListView** | `getItems()`, `getSelectionModel()`, `setCellFactory()` | `ListChangeListener` |
| **Slider** | `getValue()`, `setMin/Max()`, `setShowTickMarks()` | `ChangeListener<Number>` |
| **DatePicker** | `getValue()`, `setDayCellFactory()` | `ActionEvent` |
| **ColorPicker** | `getValue()`, `setOnAction()` | `ActionEvent` |

### Control Styling via CSS
```css
/* TextField focused state */
.text-field:focused {
    -fx-border-color: #3498db;
    -fx-effect: dropshadow(gaussian, #3498db, 5, 0, 0, 0);
}

/* Button variants */
.button-primary { -fx-background-color: #3498db; -fx-text-fill: white; }
.button-danger  { -fx-background-color: #e74c3c; -fx-text-fill: white; }
.button:disabled { -fx-opacity: 0.5; }

/* CheckBox custom */
.check-box .box { -fx-background-radius: 3; }
.check-box:selected .mark { -fx-background-color: #3498db; }

/* ComboBox dropdown */
.combo-box .list-cell { -fx-padding: 5 10; }
.combo-box-popup .list-view { -fx-background-color: white; }
```

---

## 14.4 FXML (JavaFX Markup Language)

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

## 14.5 Event Handling in Detail

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

### Event Filters (Capturing Phase) vs Event Handlers (Bubbling Phase)
> **PYQ:** Understanding the difference is important — filters run in capturing phase (parent→child), handlers in bubbling phase (child→parent).

```java
// FILTER (Capturing Phase) — runs BEFORE target, parent to child
// Use for: global shortcuts, input validation, preventing events
node.addEventFilter(KeyEvent.KEY_PRESSED, e -> {
    if (e.getCode() == KeyCode.ESCAPE) {
        e.consume();  // Prevent ESC key processing entirely
        System.out.println("ESC blocked at filter level");
    }
});

// HANDLER (Bubbling Phase) — runs AFTER target, child to parent
// Use for: actual business logic, UI updates
node.addEventHandler(KeyEvent.KEY_PRESSED, e -> {
    if (e.getCode() == KeyCode.ENTER) {
        System.out.println("Enter pressed - handler");
    }
});

// Convenience methods (handler only, bubbling phase)
button.setOnAction(e -> System.out.println("Click!"));  // Same as addEventHandler

// Event type constants for filters/handlers
KeyEvent.KEY_PRESSED, KeyEvent.KEY_RELEASED, KeyEvent.KEY_TYPED
MouseEvent.MOUSE_CLICKED, MOUSE_PRESSED, MOUSE_RELEASED, MOUSE_DRAGGED, MOUSE_MOVED, MOUSE_ENTERED, MOUSE_EXITED
ActionEvent.ACTION
DragEvent.DRAG_ENTERED, DRAG_EXITED, DRAG_OVER, DRAG_DROPPED, DRAG_DONE
ScrollEvent.SCROLL
WindowEvent.WINDOW_SHOWING, WINDOW_SHOWN, WINDOW_HIDING, WINDOW_CLOSE_REQUEST
```

### Event Handling in FXML vs Code
| Approach | Use Case | Example |
|----------|----------|---------|
| **FXML `onAction="#method"`** | Simple button clicks, menu items | `<Button onAction="#handleClick"/>` |
| **Controller `@FXML` method** | Complex logic, access to UI components | `@FXML void handleClick(ActionEvent e)` |
| **Lambda in `initialize()`** | Dynamic event binding, property listeners | `textField.textProperty().addListener(...)` |
| **`setOnAction` in code** | Non-FXML apps, dynamic UI creation | `btn.setOnAction(e -> ...)` |
| **Event Filters** | Global shortcuts, validation, blocking | `scene.addEventFilter(KeyEvent.KEY_PRESSED, ...)` |

### Event Object Key Methods
| Method | Description |
|--------|-------------|
| `getSource()` | Node that fired the event |
| `getTarget()` | Node where event occurred (may differ in bubbling) |
| `getEventType()` | Specific event type (e.g., `ActionEvent.ACTION`) |
| `consume()` | Stops further propagation (both phases) |
| `isConsumed()` | Check if already consumed |
| `copyFor(Object source, EventTarget target)` | Create copy for re-dispatching |

### Common Exam Event Handling Patterns
```java
// 1. Button click → Label update (appeared 2022, 2023, 2024, 2025, 2026)
@FXML Label outputLabel;
@FXML void handleClick(ActionEvent e) {
    outputLabel.setText("Button clicked at " + LocalTime.now());
}

// 2. TextField Enter key → Action (common)
@FXML TextField inputField;
@FXML void initialize() {
    inputField.setOnAction(e -> processInput(inputField.getText()));
}

// 3. Mouse coordinates
@FXML Pane drawingPane;
@FXML void initialize() {
    drawingPane.setOnMouseClicked(e -> {
        System.out.println("X: " + e.getX() + ", Y: " + e.getY());
        System.out.println("Screen: " + e.getScreenX() + ", " + e.getScreenY());
        System.out.println("Button: " + e.getButton()); // PRIMARY, SECONDARY, MIDDLE
        System.out.println("Click count: " + e.getClickCount()); // Double-click = 2
    });
}

// 4. Key events with modifiers
scene.addEventFilter(KeyEvent.KEY_PRESSED, e -> {
    if (e.isControlDown() && e.getCode() == KeyCode.S) {
        e.consume(); save();  // Ctrl+S shortcut
    }
});

// 5. Window close handling
stage.setOnCloseRequest(e -> {
    if (!confirmExit()) e.consume(); // Prevent close
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

## 14.6 Effects, Animation and Media

### Visual Effects (javafx.scene.effect)

#### Common Effects (with Key Properties)
```java
import javafx.scene.effect.*;
import javafx.scene.paint.Color;

// Drop Shadow — most commonly used
DropShadow shadow = new DropShadow();
shadow.setOffsetX(3);           // Horizontal offset
shadow.setOffsetY(3);           // Vertical offset
shadow.setRadius(5);            // Blur radius
shadow.setColor(Color.GRAY);    // Shadow color
shadow.setSpread(0.2);          // Sharpness (0-1)
node.setEffect(shadow);

// Inner Shadow (for pressed/inset look)
InnerShadow inner = new InnerShadow();
inner.setOffsetX(2); inner.setOffsetY(2);
inner.setRadius(4);
inner.setColor(Color.BLACK);
node.setEffect(inner);

// Glow — highlight effect (0.0 to 1.0)
Glow glow = new Glow(0.8);
node.setEffect(glow);

// Reflection — mirror effect
Reflection reflection = new Reflection();
reflection.setFraction(0.7);        // Visible fraction (0-1)
reflection.setTopOpacity(0.5);      // Top fade opacity
reflection.setBottomOpacity(0.1);   // Bottom fade opacity
reflection.setTopOffset(5);         // Gap from node
node.setEffect(reflection);

// Blur — Gaussian (smooth) or Box (fast)
GaussianBlur blur = new GaussianBlur(5);  // radius
// BoxBlur boxBlur = new BoxBlur(5, 5, 3); // width, height, iterations
node.setEffect(blur);

// Color Adjust — image/color manipulation
ColorAdjust adjust = new ColorAdjust();
adjust.setBrightness(0.2);    // -1.0 to 1.0
adjust.setContrast(0.5);      // -1.0 to 1.0
adjust.setSaturation(1.5);    // 0 to 2.0 (1.0 = normal)
adjust.setHue(0.1);           // -1.0 to 1.0
node.setEffect(adjust);

// Sepia Tone (via ColorAdjust)
ColorAdjust sepia = new ColorAdjust();
sepia.setHue(-0.1); sepia.setSaturation(0.5); sepia.setBrightness(0.1);
node.setEffect(sepia);

// Blend — combine two effects/inputs
Blend blend = new Blend();
blend.setMode(BlendMode.MULTIPLY);  // MULTIPLY, SCREEN, OVERLAY, ADD, etc.
blend.setBottomInput(new ColorInput(0, 0, 100, 100, Color.RED));
blend.setTopInput(new DropShadow());
node.setEffect(blend);

// Lighting — 3D-like shading
Light.Distant light = new Light.Distant();
light.setAzimuth(-135); light.setElevation(30);
Lighting lighting = new Lighting();
lighting.setLight(light);
lighting.setSurfaceScale(5);
node.setEffect(lighting);

// PerspectiveTransform / DisplacementMap / MotionBlur — advanced
```

#### Effect Properties Summary Table
| Effect | Key Properties | Typical Use |
|--------|----------------|-------------|
| `DropShadow` | offsetX, offsetY, radius, color, spread | Buttons, cards, depth |
| `InnerShadow` | offsetX, offsetY, radius, color | Pressed buttons, inset fields |
| `Glow` | level (0-1) | Hover highlights, focus |
| `Reflection` | fraction, top/bottomOpacity, topOffset | Mirror surfaces, logos |
| `GaussianBlur` | radius | Backgrounds, disabled state, transitions |
| `BoxBlur` | width, height, iterations | Faster blur for animation |
| `ColorAdjust` | brightness, contrast, saturation, hue | Image filters, grayscale, sepia |
| `Blend` | mode, bottomInput, topInput | Combining effects, overlays |
| `Lighting` | light, surfaceScale, diffuseConstant | 3D buttons, shapes |
| `Shadow` | (base class) | Subclass for custom shadows |

#### Effect Chaining (Correct Approach)
> **Note:** JavaFX has no `EffectChain` class. Only **one effect per node**. Chain via `Blend` or nested nodes.

```java
// Method 1: Blend two effects (most common)
Blend blend = new Blend(BlendMode.MULTIPLY, new DropShadow(), new Glow(0.5));
node.setEffect(blend);

// Method 2: Wrap in Group, apply different effects to children
Group group = new Group();
Rectangle bg = new Rectangle(100, 100, Color.BLUE);
bg.setEffect(new DropShadow());
Text text = new Text("Hello");
text.setEffect(new Glow(0.8));
group.getChildren().addAll(bg, text);

// Method 3: Layer multiple nodes with different effects
StackPane stack = new StackPane();
stack.getChildren().addAll(
    new Rectangle(100, 100, Color.BLUE).setEffect(new DropShadow()),
    new Circle(50, Color.RED).setEffect(new Glow(0.5))
);
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

## 14.7 Important Exam Questions (from PYQ Analysis 2021-2026)

> **Frequency:** JavaFX = 6/10 years | Event Handling = 5/10 years | FXML = 3/10 years | Effects/Animation/Media = 1/10 years (2025)

### 2-Mark Questions (Short Answer / Differentiate)
1. **JavaFX vs AWT vs Swing** — 3 key differences (rendering, components, features)
2. **JavaFX Architecture** — Stage, Scene, Scene Graph, Prism, Glass
3. **Layout Panes** — Name 4 layouts and their use cases (HBox, VBox, BorderPane, GridPane) — **2026 Q1(g)**
4. **FXML** — What is it? Key attributes: `fx:id`, `fx:controller`, `onAction`, `styleClass`
5. **Scene Builder** — Visual FXML editor, drag-drop, generates XML
6. **Event Handling Approaches** — Lambda, EventHandler interface, FXML controller
7. **Event Filter vs Handler** — Filter = capturing (parent→child), Handler = bubbling (child→parent)
8. **`consume()` method** — Stops event propagation
9. **CSS in JavaFX** — `-fx-` prefix; 3 ways: inline, styleClass, ID
10. **Pseudo-classes** — `:hover`, `:pressed`, `:focused`, `:disabled`
11. **Timeline vs Transitions** — Timeline = keyframe-based (custom), Transitions = pre-built (Translate, Rotate, Scale, Fade)
12. **Parallel vs Sequential Transition** — Parallel = simultaneous, Sequential = one after another
13. **Media classes** — Media, MediaPlayer, MediaView
14. **Common Effects** — DropShadow, Glow, Reflection, Blur, ColorAdjust

### 5-Mark Questions (Short Notes / Explain with Example)
1. **JavaFX Features** — GPU rendering, FXML, CSS, Animation, Media, 3D, WebView, Scene Builder — **2021, 2023, 2025, 2026**
2. **AWT vs Swing vs JavaFX** — Comparison table — **2022, 2023, 2025**
3. **Layout Panes** — Explain HBox, VBox, BorderPane, GridPane with code — **2026**
4. **FXML Structure & Controller** — XML structure, `fx:controller`, `@FXML`, `initialize()` — **2024**
5. **CSS Styling** — 3 methods, pseudo-classes, example — **2024, 2025**
6. **Event Handling** — Lambda, EventHandler, FXML; filters vs handlers; phases — **2022, 2023, 2024, 2025, 2026**
7. **JavaFX Effects** — DropShadow, Glow, Reflection, Blur, ColorAdjust with code — **2025**
8. **Animation: Timeline & Transitions** — KeyFrame/KeyValue, Translate/Rotate/Scale/Fade, Parallel/Sequential — **2025**
9. **MediaPlayer** — Audio/Video playback, controls, events — **2025**
10. **GUI Program** — Name/Email input + Button click → Label update — **2022, 2025**

### 10-Mark Questions (Detailed Theory + Complete Program)
1. **Complete JavaFX MVC Application** — FXML + CSS + Controller + Layout + Controls + Event Handling + Animation — **2024, 2025, 2026**
2. **Event Handling Deep Dive** — Hierarchy, phases, filters vs handlers, lambda, FXML, consume(), examples — **2024 (10m)**
3. **JavaFX Architecture + Features + Components + Layouts** — Full theory — **2021 (10m), 2026 (5m)**

### Programs to Practice (High Yield)
1. ✅ **CSS styled form (style.css + Java)** — appeared 2024, 2025
2. ✅ **FXML login form with controller** — appeared 2024, 2025, 2026
3. ✅ **Event handling (Button click → Label update)** — appeared 2022, 2023, 2024, 2025, 2026
4. ✅ **GUI Name/Email + Button** — appeared 2022, 2025
5. ✅ **Effects (DropShadow, Glow, Reflection)** — appeared 2025
6. ✅ **Animation (TranslateTransition, FadeTransition, Parallel)** — appeared 2025
7. ✅ **MediaPlayer (audio/video)** — appeared 2025
8. ✅ **Complete MVC App (FXML + CSS + Controller + Animation)** — 10-mark standard

---

## 14.8 Summary of Unit 14

| Topic | Key Points |
|-------|------------|
| **JavaFX Architecture** | Stage → Scene → Scene Graph (Node tree); Prism GPU pipeline; Glass windowing; MVC via FXML |
| **AWT vs Swing vs JavaFX** | AWT=heavyweight/OS; Swing=lightweight/CPU; JavaFX=lightweight/GPU + FXML + CSS + Media + 3D |
| **Layout Panes** | HBox, VBox, BorderPane, GridPane, FlowPane, StackPane, TilePane, AnchorPane — **asked 2026** |
| **UI Controls** | Button, Label, TextField, PasswordField, TextArea, CheckBox, RadioButton, ComboBox, ListView, Slider, DatePicker, ColorPicker |
| **CSS** | `-fx-` prefix; inline, styleClass, ID; pseudo-classes (:hover, :pressed, :focused, :disabled) |
| **FXML** | XML for UI; `fx:id`, `fx:controller`, `onAction`; Scene Builder; `@FXML` injection |
| **Controller** | `@FXML` injection; `initialize()`; event handlers; property listeners |
| **Event Handling** | Lambda (preferred), EventHandler, FXML `onAction`; **filters (capture) vs handlers (bubble)**; `consume()` |
| **Effects** | DropShadow, InnerShadow, Glow, Reflection, GaussianBlur, ColorAdjust, Blend, Lighting |
| **Animation** | Timeline (KeyFrames), Transitions (Translate, Rotate, Scale, Fade, Parallel, Sequential, Pause) |
| **Media** | Media, MediaPlayer, MediaView; audio/video; progress, seek, volume, rate |
| **Integration** | FXML + CSS + Controller = MVC pattern — **10-mark program standard** |

---

## 14.9 Complete Integrated Example (10-Mark Program Pattern)

> **PYQ:** "Complete JavaFX app with FXML, CSS, event handling, animation" — 2024, 2025, 2026

This example demonstrates the **full MVC stack** examiners expect: **FXML (View) + CSS (Style) + Controller (Logic) + Layout + Controls + Event Handling + Animation**.

### 1. Main Application Class
```java
package com.exam;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class StudentApp extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("student.fxml"));
        Parent root = loader.load();
        
        Scene scene = new Scene(root);
        scene.getStylesheets().add(getClass().getResource("style.css").toExternalForm());
        
        stage.setTitle("Student Registration (MVC + CSS + Animation)");
        stage.setScene(scene);
        stage.show();
    }
    
    public static void main(String[] args) { launch(args); }
}
```

### 2. FXML View (student.fxml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?import javafx.scene.layout.*?>
<?import javafx.scene.control.*?>
<?import javafx.geometry.*?>

<BorderPane xmlns:fx="http://javafx.com/fxml/1" 
            fx:controller="com.exam.StudentController"
            styleClass="root">
    <top>
        <Label text="Student Registration Form" styleClass="title-label" 
               BorderPane.alignment="CENTER"/>
    </top>
    
    <center>
        <VBox spacing="15" alignment="CENTER" styleClass="form-container">
            <padding><Insets top="20" right="20" bottom="20" left="20"/></padding>
            
            <GridPane hgap="10" vgap="10" alignment="CENTER">
                <Label text="Name:" styleClass="form-label" GridPane.columnIndex="0" GridPane.rowIndex="0"/>
                <TextField fx:id="nameField" promptText="Enter name" styleClass="text-field" 
                           GridPane.columnIndex="1" GridPane.rowIndex="0"/>
                
                <Label text="Email:" styleClass="form-label" GridPane.columnIndex="0" GridPane.rowIndex="1"/>
                <TextField fx:id="emailField" promptText="Enter email" styleClass="text-field" 
                           GridPane.columnIndex="1" GridPane.rowIndex="1"/>
                
                <Label text="Course:" styleClass="form-label" GridPane.columnIndex="0" GridPane.rowIndex="2"/>
                <ComboBox fx:id="courseBox" styleClass="combo-box" GridPane.columnIndex="1" GridPane.rowIndex="2"/>
            </GridPane>
            
            <HBox spacing="10" alignment="CENTER">
                <Button text="Register" fx:id="registerBtn" styleClass="button primary" 
                        onAction="#handleRegister"/>
                <Button text="Clear" fx:id="clearBtn" styleClass="button secondary" 
                        onAction="#handleClear"/>
                <Button text="Animate" fx:id="animateBtn" styleClass="button accent" 
                        onAction="#handleAnimate"/>
            </HBox>
            
            <Label fx:id="statusLabel" styleClass="status-label" text=" "/>
            
            <ProgressBar fx:id="progressBar" prefWidth="300" progress="0.0" visible="false"/>
        </VBox>
    </center>
    
    <bottom>
        <Label fx:id="footerLabel" text="MCS-206 JavaFX Demo" styleClass="footer-label" 
               BorderPane.alignment="CENTER"/>
    </bottom>
</BorderPane>
```

### 3. CSS Styling (style.css)
```css
.root {
    -fx-background-color: linear-gradient(to bottom, #f5f7fa, #e4e8eb);
    -fx-font-family: "Segoe UI", "Arial", sans-serif;
    -fx-font-size: 14px;
}

.title-label {
    -fx-font-size: 24px;
    -fx-font-weight: bold;
    -fx-text-fill: #2c3e50;
    -fx-padding: 20 0;
    -fx-effect: dropshadow(gaussian, rgba(0,0,0,0.1), 2, 0, 0, 1);
}

.form-container {
    -fx-background-color: white;
    -fx-background-radius: 10;
    -fx-effect: dropshadow(gaussian, rgba(0,0,0,0.15), 10, 0, 0, 5);
    -fx-padding: 20;
}

.form-label {
    -fx-text-fill: #34495e;
    -fx-font-weight: 600;
}

.text-field {
    -fx-background-color: white;
    -fx-border-color: #bdc3c7;
    -fx-border-radius: 5;
    -fx-background-radius: 5;
    -fx-padding: 8 12;
    -fx-pref-width: 250;
}

.text-field:focused {
    -fx-border-color: #3498db;
    -fx-effect: dropshadow(gaussian, #3498db, 8, 0, 0, 0);
}

.combo-box {
    -fx-pref-width: 250;
    -fx-background-radius: 5;
    -fx-border-radius: 5;
    -fx-border-color: #bdc3c7;
}

.button {
    -fx-font-size: 13px;
    -fx-font-weight: 600;
    -fx-padding: 10 24;
    -fx-border-radius: 5;
    -fx-background-radius: 5;
    -fx-cursor: hand;
    -fx-text-fill: white;
    -fx-effect: dropshadow(gaussian, rgba(0,0,0,0.2), 3, 0, 0, 2);
}

.button.primary { -fx-background-color: #27ae60; }
.button.primary:hover { -fx-background-color: #219653; }
.button.primary:pressed { -fx-background-color: #1e824c; }

.button.secondary { -fx-background-color: #95a5a6; }
.button.secondary:hover { -fx-background-color: #7f8c8d; }

.button.accent { -fx-background-color: #3498db; }
.button.accent:hover { -fx-background-color: #2980b9; }

.button:disabled { -fx-opacity: 0.5; -fx-cursor: default; }

.status-label {
    -fx-font-size: 13px;
    -fx-text-fill: #27ae60;
    -fx-min-height: 20px;
}

.progress-bar .bar {
    -fx-background-color: #27ae60;
    -fx-background-radius: 2;
}

.progress-bar .track {
    -fx-background-color: #ecf0f1;
    -fx-background-radius: 2;
}

.footer-label {
    -fx-text-fill: #7f8c8d;
    -fx-font-size: 11px;
    -fx-padding: 10;
}
```

### 4. Controller with Event Handling + Animation
```java
package com.exam;

import javafx.animation.*;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.util.Duration;
import javafx.geometry.Pos;

public class StudentController {
    @FXML private TextField nameField, emailField;
    @FXML private ComboBox<String> courseBox;
    @FXML private Button registerBtn, clearBtn, animateBtn;
    @FXML private Label statusLabel, footerLabel;
    @FXML private ProgressBar progressBar;
    
    @FXML
    public void initialize() {
        // Setup ComboBox
        courseBox.getItems().addAll("MCS-201", "MCS-202", "MCS-203", "MCS-204", "MCS-205", "MCS-206");
        courseBox.setPromptText("Select course");
        
        // Default button behavior
        registerBtn.setDefaultButton(true);
        clearBtn.setCancelButton(true);
        
        // Input validation on typing
        nameField.textProperty().addListener((obs, old, val) -> validateForm());
        emailField.textProperty().addListener((obs, old, val) -> validateForm());
        courseBox.valueProperty().addListener((obs, old, val) -> validateForm());
    }
    
    private void validateForm() {
        boolean valid = !nameField.getText().trim().isEmpty() 
                     && !emailField.getText().trim().isEmpty()
                     && courseBox.getValue() != null;
        registerBtn.setDisable(!valid);
    }
    
    @FXML
    private void handleRegister() {
        String name = nameField.getText().trim();
        String email = emailField.getText().trim();
        String course = courseBox.getValue();
        
        // Simulate registration with progress animation
        showProgress("Registering " + name + " for " + course + "...", () -> {
            statusLabel.setText("✓ Registered: " + name + " (" + email + ") - " + course);
            statusLabel.setStyle("-fx-text-fill: #27ae60;");
            
            // Fade out status after 3 seconds
            FadeTransition fade = new FadeTransition(Duration.seconds(1), statusLabel);
            fade.setFromValue(1.0);
            fade.setToValue(0.0);
            fade.setDelay(Duration.seconds(3));
            fade.setOnFinished(e -> statusLabel.setText(" "));
            fade.play();
        });
    }
    
    @FXML
    private void handleClear() {
        nameField.clear();
        emailField.clear();
        courseBox.getSelectionModel().clearSelection();
        statusLabel.setText("Form cleared");
        statusLabel.setStyle("-fx-text-fill: #e74c3c;");
        registerBtn.setDisable(true);
    }
    
    @FXML
    private void handleAnimate() {
        // Parallel animation: fade + translate + scale on status label
        FadeTransition fade = new FadeTransition(Duration.millis(500), statusLabel);
        fade.setFromValue(0.0); fade.setToValue(1.0);
        fade.setCycleCount(4); fade.setAutoReverse(true);
        
        TranslateTransition slide = new TranslateTransition(Duration.millis(500), statusLabel);
        slide.setFromX(-50); slide.setToX(0);
        slide.setCycleCount(2); slide.setAutoReverse(true);
        
        ScaleTransition scale = new ScaleTransition(Duration.millis(500), statusLabel);
        scale.setFromX(0.8); scale.setToX(1.2);
        scale.setFromY(0.8); scale.setToY(1.2);
        scale.setCycleCount(4); scale.setAutoReverse(true);
        
        ParallelTransition parallel = new ParallelTransition(statusLabel, fade, slide, scale);
        parallel.setOnFinished(e -> {
            statusLabel.setText("Animation complete!");
            statusLabel.setStyle("-fx-text-fill: #3498db;");
        });
        parallel.play();
    }
    
    private void showProgress(String message, Runnable onComplete) {
        progressBar.setVisible(true);
        progressBar.setProgress(-1.0); // Indeterminate
        statusLabel.setText(message);
        statusLabel.setStyle("-fx-text-fill: #3498db;");
        
        // Simulate async work
        PauseTransition pause = new PauseTransition(Duration.seconds(2));
        pause.setOnFinished(e -> {
            progressBar.setVisible(false);
            progressBar.setProgress(0.0);
            onComplete.run();
        });
        pause.play();
    }
}
```

---

## 14.10 Quick Reference: JavaFX CSS Properties

```css
/* ===== COLORS ===== */
-fx-background-color: #3498db;           /* Solid */
-fx-background-color: rgba(52,152,219,0.8);  /* With alpha */
-fx-background-color: linear-gradient(to bottom, #3498db, #2980b9); /* Gradient */
-fx-background-color: radial-gradient(center 50% 50%, radius 50%, #3498db, #2980b9); /* Radial */
-fx-text-fill: white;
-fx-border-color: #2c3e50;

/* ===== FONTS ===== */
-fx-font-size: 14px;                     /* px, pt, em, % */
-fx-font-family: "Segoe UI", "Arial", sans-serif;  /* Fallback chain */
-fx-font-weight: bold;                   /* normal, bold, bolder, lighter, 100-900 */
-fx-font-style: italic;                  /* normal, italic */
-fx-font: bold 14px "Segoe UI";          /* Shorthand */

/* ===== LAYOUT (Region/Pane) ===== */
-fx-padding: 10 20 10 20;                /* Top Right Bottom Left */
-fx-padding: 10 20;                      /* Vertical Horizontal */
-fx-padding: 10;                         /* All sides */
-fx-spacing: 10;                         /* HBox/VBox/FlowPane gap */
-fx-alignment: center;                   /* top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right, baseline-left, baseline-center, baseline-right */
-fx-min-width: 100; -fx-pref-width: 200; -fx-max-width: 300;
-fx-min-height: 50; -fx-pref-height: 100; -fx-max-height: 200;

/* ===== BORDERS & RADIUS ===== */
-fx-border-width: 2px;                   /* or: 2 4 2 4 (TB LR) */
-fx-border-style: solid;                 /* solid, dashed, dotted, none */
-fx-border-color: #2c3e50;
-fx-border-radius: 5;                    /* or: 5 10 5 10 (TL TR BR BL) */
-fx-background-radius: 5;                /* Background corner radius */
-fx-border-insets: 0;                    /* Border inset from edge */

/* ===== BACKGROUNDS ===== */
-fx-background-image: url("bg.png");
-fx-background-repeat: no-repeat;        /* repeat, repeat-x, repeat-y, no-repeat */
-fx-background-position: center center;  /* left top, center, right bottom, etc. */
-fx-background-size: cover;              /* cover, contain, auto, 100px 100px */

/* ===== TEXT & LABEL ===== */
-fx-text-alignment: center;              /* left, center, right, justify */
-fx-text-overrun: ellipsis;              /* clip, ellipsis, leading-ellipsis, center-ellipsis */
-fx-wrap-text: true;                     /* Multi-line wrapping */
-fx-line-spacing: 2;                     /* Extra space between lines */
-fx-underline: true;                     /* Underline text */
-fx-strikethrough: false;                /* Strikethrough */

/* ===== EFFECTS (CSS) ===== */
-fx-opacity: 0.8;                        /* 0.0 to 1.0 */
-fx-effect: dropshadow(gaussian, rgba(0,0,0,0.3), 10, 0, 0, 2);  /* gaussian/one-pass-box/three-pass-box/two-pass-box */
-fx-effect: innershadow(gaussian, black, 5, 0, 0, 2);
-fx-blend-mode: multiply;                /* src-over, multiply, screen, overlay, darken, lighten, etc. */
-fx-clip: rect(0, 100, 100, 0);          /* Clipping rectangle */

/* ===== CURSOR ===== */
-fx-cursor: hand;                        /* default, crosshair, text, wait, move, ne-resize, nw-resize, se-resize, sw-resize, n-resize, s-resize, e-resize, w-resize, none */

/* ===== STATES (Pseudo-classes) ===== */
.button:hover { -fx-background-color: #2980b9; }
.button:pressed { -fx-background-color: #1c6ea4; }
.button:focused { -fx-border-color: #3498db; -fx-border-width: 2px; }
.button:disabled { -fx-opacity: 0.5; -fx-cursor: default; }
.button:armed { -fx-background-color: #1c6ea4; }    /* Mouse pressed but not released */
.button:default { -fx-border-color: #3498db; }       /* Default button (Enter key) */
.text-field:focused { -fx-border-color: #3498db; -fx-effect: dropshadow(gaussian, #3498db, 5, 0, 0, 0); }
.text-field:disabled { -fx-opacity: 0.5; -fx-background-color: #ecf0f1; }
.check-box:selected .mark { -fx-background-color: #27ae60; }
.list-cell:filled:selected { -fx-background-color: #3498db; -fx-text-fill: white; }
.tab:selected { -fx-background-color: white; }

/* ===== SPECIFIC CONTROL STYLING ===== */
/* ScrollBar */
.scroll-bar { -fx-background-color: transparent; }
.scroll-bar .thumb { -fx-background-color: #bdc3c7; -fx-background-radius: 5; }
.scroll-bar .thumb:hover { -fx-background-color: #95a5a6; }

/* Slider */
.slider .track { -fx-background-color: #ecf0f1; -fx-background-radius: 2; }
.slider .thumb { -fx-background-color: #3498db; -fx-background-radius: 50%; }

/* ProgressBar */
.progress-bar .track { -fx-background-color: #ecf0f1; -fx-background-radius: 2; }
.progress-bar .bar { -fx-background-color: #27ae60; -fx-background-radius: 2; }

/* ComboBox */
.combo-box { -fx-background-color: white; -fx-border-color: #bdc3c7; -fx-border-radius: 5; }
.combo-box .arrow-button { -fx-background-color: transparent; }
.combo-box-popup .list-view { -fx-background-color: white; -fx-effect: dropshadow(gaussian, rgba(0,0,0,0.2), 10, 0, 0, 5); }

/* Tooltip */
.tooltip { -fx-background-color: #2c3e50; -fx-text-fill: white; -fx-padding: 8 12; -fx-background-radius: 5; }

/* ContextMenu */
.context-menu { -fx-background-color: white; -fx-effect: dropshadow(gaussian, rgba(0,0,0,0.2), 10, 0, 0, 5); }
.menu-item:hover { -fx-background-color: #ecf0f1; }

/* ===== REGION STYLES (for custom shapes) ===== */
-fx-shape: "M 0 0 L 100 0 L 100 100 L 0 100 Z";  /* SVG path */
-fx-scale-shape: true;
-fx-center-shape: true;
```