# Unit 13: Introduction to GUI in Java

## Unit Overview
This unit covers AWT, Swing, and JavaFX APIs for GUI development, including components, layouts, event handling, and JavaFX features.

---

## 13.1 GUI APIs in Java

### Three Main GUI APIs

| API | Introduced | Characteristics |
|-----|------------|-----------------|
| **AWT** (Abstract Window Toolkit) | JDK 1.0 | Heavyweight, platform-dependent, limited components |
| **Swing** | JDK 1.2 (JFC) | Lightweight, platform-independent, MVC, pluggable look & feel |
| **JavaFX** | JDK 8 (separate from JDK 11+) | Modern, rich UI, CSS styling, FXML, hardware acceleration |

### Comparison

| Feature | AWT | Swing | JavaFX |
|---------|-----|-------|--------|
| **Weight** | Heavyweight | Lightweight | Lightweight |
| **Platform** | Dependent | Independent | Independent |
| **Components** | Basic | Rich | Rich + Modern |
| **Look & Feel** | Native OS | Pluggable | CSS-based |
| **Architecture** | Peer-based | MVC | Scene Graph |
| **Styling** | Limited | UIManager | CSS |
| **Layout** | LayoutManager | LayoutManager | Pane-based |
| **Performance** | Slow | Moderate | GPU-accelerated |
| **Current Status** | Legacy | Maintenance | **Recommended** |

---

## 13.2 AWT (Abstract Window Toolkit)

### AWT Hierarchy
```
Object
  │
  └─ Component (abstract)
       │
       ├─ Button
       ├─ Label
       ├─ TextField
       ├─ TextArea
       ├─ Checkbox
       ├─ Choice
       ├─ List
       ├─ Scrollbar
       └─ Container
            │
            ├─ Panel
            ├─ Window
            │    │
            │    ├─ Frame
            │    └─ Dialog
            ├─ Applet
            └─ ScrollPane
```

### Key Classes

| Class | Description |
|-------|-------------|
| **Component** | Abstract base; encapsulates visual component attributes |
| **Container** | Holds other components; manages layout |
| **Panel** | Concrete Container; no title bar/border |
| **Window** | Top-level window; no title bar |
| **Frame** | Top-level window; title bar, menu bar, borders |
| **Button** | Push button |
| **Label** | Text display (non-editable) |
| **TextField** | Single-line text input |
| **TextArea** | Multi-line text input |
| **Checkbox** | On/off toggle |
| **Choice** | Dropdown list |
| **List** | Multiple item selection |
| **Scrollbar** | Scroll control |

### AWT Example
```java
import java.awt.*;
import java.awt.event.*;

public class AWTExample extends Frame implements WindowListener {
    AWTExample() {
        setTitle("AWT Example");
        setSize(400, 300);
        setLayout(new FlowLayout());
        
        Label label = new Label("Welcome to AWT");
        Button btn = new Button("Click Me");
        TextField tf = new TextField(20);
        
        add(label);
        add(tf);
        add(btn);
        
        addWindowListener(this);
        setVisible(true);
    }
    
    public void windowClosing(WindowEvent e) {
        dispose();
        System.exit(0);
    }
    // Other WindowListener methods empty...
    
    public static void main(String[] args) {
        new AWTExample();
    }
}
```

---

## 13.3 Swing

### Swing Hierarchy
```
Object
  │
  └─ Component (AWT)
       │
       └─ Container (AWT)
            │
            └─ JComponent (Swing base)
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
      JButton  JLabel   JTextField
      JList    JTable   JPanel
      JFrame   JDialog  JApplet
```

### Key Features
- **Lightweight**: Written in pure Java
- **Pluggable Look & Feel**: Metal, Nimbus, Windows, Mac
- **MVC Architecture**: Model-View-Controller separation
- **Rich Components**: JTable, JTree, JTabbedPane, JColorChooser, etc.

### Common Components
| Component | Description |
|-----------|-------------|
| `JFrame` | Main window (replaces Frame) |
| `JPanel` | Container (replaces Panel) |
| `JButton` | Button |
| `JLabel` | Label |
| `JTextField` | Single-line input |
| `JTextArea` | Multi-line input |
| `JCheckBox` | Checkbox |
| `JRadioButton` | Radio button |
| `JComboBox` | Dropdown |
| `JList` | List |
| `JTable` | Table |
| `JScrollPane` | Scrollable container |

### Swing Example
```java
import javax.swing.*;
import java.awt.*;

public class SwingExample extends JFrame {
    SwingExample() {
        setTitle("Swing Example");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        
        JLabel label = new JLabel("Welcome to Swing");
        JButton btn = new JButton("Click Me");
        JTextField tf = new JTextField(20);
        
        add(label);
        add(tf);
        add(btn);
        
        setVisible(true);
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new SwingExample());
    }
}
```

---

## 13.4 JavaFX

### Overview
- **Modern GUI platform** for rich client applications
- **Scene Graph** architecture (tree of nodes)
- **CSS Styling** for appearance
- **FXML** for declarative UI definition
- **MVC Pattern**: Model (data) - View (FXML) - Controller (Java)

### JavaFX Architecture
```
Application
    │
    ├─ Stage (Top-level window)
    │    │
    │    └─ Scene (Container for content)
    │         │
    │         └─ Root Node (Layout Pane)
    │              │
    │              ├─ Controls (Buttons, Labels, etc.)
    │              ├─ Shapes (Circle, Rectangle, etc.)
    │              ├─ Media (ImageView, MediaView)
    │              └─ Effects, Transforms
    │
    └─ CSS Stylesheets
```

### JavaFX Application Structure
```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

public class JavaFXExample extends Application {
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("JavaFX Example");
        
        Label label = new Label("Welcome to JavaFX");
        Button btn = new Button("Click Me");
        
        VBox root = new VBox(10, label, btn);  // Vertical layout, 10px spacing
        root.setStyle("-fx-padding: 20; -fx-alignment: center;");
        
        Scene scene = new Scene(root, 400, 300);
        // scene.getStylesheets().add("styles.css");
        
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

## 13.5 JavaFX Features

### Key Features (JavaFX 8+)
1. **FXML** - XML-based UI markup
2. **CSS Styling** - Web-style styling
3. **Scene Builder** - Visual UI designer
4. **Properties & Binding** - Observable properties
5. **Animations & Transitions** - Timeline, TranslateTransition, etc.
6. **3D Graphics** - Box, Sphere, Cylinder, MeshView
7. **Media Support** - Audio, Video (MediaPlayer, MediaView)
8. **WebView** - Embedded browser (WebKit)
9. **Printing API** - javafx.print
10. **Touch & Gestures** - Multi-touch support

---

## 13.6 JavaFX UI Components (Controls)

### Common Controls
| Control | Description |
|---------|-------------|
| `Label` | Non-editable text |
| `Button` | Action button |
| `TextField` | Single-line input |
| `PasswordField` | Masked input |
| `TextArea` | Multi-line input |
| `CheckBox` | Boolean toggle |
| `RadioButton` | Exclusive selection |
| `ToggleButton` | Toggle state |
| `ComboBox` | Dropdown selection |
| `ChoiceBox` | Simple dropdown |
| `ListView` | List of items |
| `TableView` | Tabular data |
| `TreeView` | Hierarchical data |
| `DatePicker` | Calendar date selection |
| `ColorPicker` | Color selection |
| `Slider` | Numeric range |
| `ProgressBar` | Progress indication |
| `MenuBar` / `Menu` / `MenuItem` | Menus |
| `ToolBar` | Tool buttons |
| `TabPane` | Tabbed interface |
| `SplitPane` | Resizable panes |
| `Accordion` | Collapsible panes |
| `TitledPane` | Collapsible titled panel |

---

## 13.7 JavaFX Layouts (Panes)

| Layout | Description | Use Case |
|--------|-------------|----------|
| `VBox` | Vertical column | Forms, stacking |
| `HBox` | Horizontal row | Toolbars, button groups |
| `BorderPane` | Top, Left, Center, Right, Bottom | Main window layout |
| `GridPane` | Grid of rows/columns | Forms, calculators |
| `FlowPane` | Flowing wrap | Tag clouds, responsive |
| `TilePane` | Uniform tiles | Galleries, icon grids |
| `StackPane` | Stacked (z-order) | Overlays, centering |
| `AnchorPane` | Anchored to edges | Precise positioning |
| `TilePane` | Uniform grid | Photo grids |

### Layout Examples
```java
// VBox - Vertical
VBox vbox = new VBox(10);  // 10px spacing
vbox.getChildren().addAll(label, textField, button);

// HBox - Horizontal
HBox hbox = new HBox(10);
hbox.getChildren().addAll(okBtn, cancelBtn);

// BorderPane
BorderPane border = new BorderPane();
border.setTop(menuBar);
border.setLeft(sideBar);
border.setCenter(contentArea);
border.setBottom(statusBar);

// GridPane - Form layout
GridPane grid = new GridPane();
grid.setHgap(10); grid.setVgap(10);
grid.add(new Label("Name:"), 0, 0);
grid.add(nameField, 1, 0);
grid.add(new Label("Email:"), 0, 1);
grid.add(emailField, 1, 1);
```

---

## 13.8 Event Handling in JavaFX

### Event Handling Mechanisms

#### 1. Lambda Expression (Recommended)
```java
Button btn = new Button("Click Me");
btn.setOnAction(event -> {
    System.out.println("Button clicked!");
    label.setText("Clicked!");
});
```

#### 2. EventHandler Interface
```java
btn.setOnAction(new EventHandler<ActionEvent>() {
    @Override
    public void handle(ActionEvent event) {
        System.out.println("Clicked!");
    }
});
```

#### 3. FXML Controller (Separate class)
```java
// Controller.java
public class Controller {
    @FXML private Label label;
    @FXML private Button btn;
    
    @FXML
    public void handleClick(ActionEvent event) {
        label.setText("Clicked from FXML!");
    }
}
```

### Common Event Types
| Event | Description |
|-------|-------------|
| `ActionEvent` | Button click, menu select |
| `MouseEvent` | Click, drag, move, enter/exit |
| `KeyEvent` | Key press, release, type |
| `DragEvent` | Drag and drop |
| `ScrollEvent` | Scroll wheel |
| `WindowEvent` | Show, hide, close |

### Event Phases
1. **Route Construction** - Build path from source to root
2. **Event Capturing** - Root → Target (capture phase)
3. **Event Targeting** - At target node
4. **Event Bubbling** - Target → Root (bubble phase)

---

## 13.9 Adding HTML Content, Text and Text Effects

### WebView (HTML Content)
```java
import javafx.scene.web.WebView;
import javafx.scene.web.WebEngine;

WebView webView = new WebView();
WebEngine engine = webView.getEngine();
engine.load("https://www.example.com");
// Or load HTML string:
// engine.loadContent("<h1>Hello HTML</h1>");
```

### Text Node
```java
import javafx.scene.text.Text;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.paint.Color;

Text text = new Text("Styled Text");
text.setFont(Font.font("Arial", FontWeight.BOLD, 24));
text.setFill(Color.BLUE);
text.setX(50);
text.setY(100);
```

### Text Effects
```java
import javafx.scene.effect.*;

// Drop Shadow
DropShadow shadow = new DropShadow();
shadow.setOffsetX(3);
shadow.setOffsetY(3);
shadow.setColor(Color.GRAY);
text.setEffect(shadow);

// Glow
Glow glow = new Glow(0.8);
text.setEffect(glow);

// Reflection
Reflection reflection = new Reflection();
reflection.setFraction(0.7);
text.setEffect(reflection);

// Blend
Blend blend = new Blend();
blend.setMode(BlendMode.MULTIPLY);
```

---

## 13.10 Important Exam Questions (from PYQ Analysis)

### High Priority

**2-Mark Questions:**
1. Difference between AWT and Swing.
2. Difference between Swing and JavaFX.
3. What is JavaFX? Key features.
4. What is FXML? What is Scene Builder?
5. What are layout panes in JavaFX?
6. How to handle events in JavaFX?
7. What is Scene Graph?
8. Difference between Stage and Scene.

**5-Mark Questions:**
1. Explain AWT, Swing, JavaFX with differences.
2. Explain JavaFX features and architecture.
3. Explain JavaFX layouts with examples.
4. Explain event handling in JavaFX with lambda.
5. Write a JavaFX program with Button and Label.
6. Explain CSS styling in JavaFX.

**10-Mark Questions:**
1. **Explain AWT vs Swing vs JavaFX. JavaFX features, components, layouts, event handling, CSS/FXML.** (Appeared 2021, 2022, 2023, 2024, 2025, 2026)
2. Complete JavaFX application with MVC, FXML, event handling.

### Programs to Practice
1. ✅ **JavaFX Hello World (Stage, Scene, Label, Button)** - appeared 2021, 2022, 2023, 2024, 2025, 2026
2. ✅ **Event handling (Button click → Label change)** - appeared 2022, 2023, 2024, 2025, 2026
3. ✅ **Layouts (VBox, HBox, BorderPane, GridPane)** - appeared 2024, 2025, 2026
4. ✅ **Name/Email input form (GridPane)** - appeared 2022, 2025
5. ✅ **CSS styling in JavaFX** - appeared 2024, 2025

---

## 13.11 Summary of Unit 13

| Topic | Key Points |
|-------|------------|
| **AWT** | Heavyweight, platform-dependent, basic components |
| **Swing** | Lightweight, pluggable L&F, MVC, rich components |
| **JavaFX** | Modern, Scene Graph, CSS, FXML, hardware accelerated |
| **JavaFX Architecture** | Application → Stage → Scene → Root Node → Controls |
| **Layouts** | VBox, HBox, BorderPane, GridPane, FlowPane, StackPane, AnchorPane |
| **Controls** | Label, Button, TextField, ComboBox, TableView, DatePicker, etc. |
| **Event Handling** | Lambda (preferred), EventHandler, FXML Controller |
| **FXML** | XML-based UI; separates view from logic |
| **CSS** | Web-style styling; -fx- prefix for properties |
| **Effects** | DropShadow, Glow, Reflection, Blend, etc. |
| **Media** | MediaPlayer, MediaView for audio/video |
| **WebView** | Embedded WebKit browser |

---

## 13.12 Quick Reference: JavaFX Application Template

```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.geometry.*;

public class MyApp extends Application {
    @Override
    public void start(Stage stage) {
        // 1. Create controls
        Label label = new Label("Hello");
        Button btn = new Button("Click");
        
        // 2. Create layout
        VBox root = new VBox(10, label, btn);
        root.setAlignment(Pos.CENTER);
        root.setPadding(new Insets(20));
        
        // 3. Create scene
        Scene scene = new Scene(root, 400, 300);
        // scene.getStylesheets().add("style.css");
        
        // 4. Configure stage
        stage.setTitle("My App");
        stage.setScene(scene);
        stage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```