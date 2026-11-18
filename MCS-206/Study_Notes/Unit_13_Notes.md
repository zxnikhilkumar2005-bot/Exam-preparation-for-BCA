# Unit 13: Introduction to GUI in Java

> **PYQ Weightage**: 10–20 marks | **Frequency**: 7/10 years | **Critical Priority** - This topic appears almost every year in 10-mark and 5-mark questions.

## Unit Overview
This unit covers AWT, Swing, and JavaFX APIs for GUI development, including components, layouts, event handling, CSS styling, and FXML.

---

## 13.1 GUI APIs in Java

### Three Main GUI APIs

| API | Introduced | Characteristics |
|-----|------------|-----------------|
| **AWT** (Abstract Window Toolkit) | JDK 1.0 | Heavyweight, platform-dependent, basic components |
| **Swing** | JDK 1.2 (JFC) | Lightweight, platform-independent, MVC, pluggable look & feel |
| **JavaFX** | JDK 8 (separate from JDK 11+) | Modern, rich UI, CSS styling, FXML, Scene Graph, hardware acceleration |

### Comparison Table (Exam Important)

| Feature | AWT | Swing | JavaFX |
|---------|-----|-------|--------|
| **Weight** | Heavyweight (uses native OS peers) | Lightweight (pure Java) | Lightweight (Scene Graph) |
| **Platform** | Dependent | Independent | Independent |
| **Components** | Basic (Button, Label, TextField) | Rich (JTable, JTree, JTabbedPane, JComboBox, etc.) | Rich + Modern (TableView, DatePicker, Charts, 3D, Media) |
| **Look & Feel** | Native OS (fixed) | Pluggable (Metal, Nimbus, Windows, Mac) | CSS-based, highly customizable |
| **Architecture** | Peer-based | MVC (Model-View-Controller) | Scene Graph (tree of Nodes) |
| **Styling** | Limited (no CSS) | UIManager / UIDefaults | CSS with `-fx-` prefix |
| **Layout** | LayoutManager interfaces | LayoutManager (Flow, Border, Grid, etc.) | Pane-based (VBox, HBox, BorderPane, GridPane, etc.) |
| **Performance** | Slow (native peer overhead) | Moderate | GPU-accelerated (Prism pipeline) |
| **Event Model** | Delegation (Action, Mouse, etc.) | Same + Action architecture | Modern event delivery (capture/target/bubble phases) |
| **Current Status** | Legacy (maintenance only) | Maintenance mode | **Recommended** for new applications |
| **FXML Support** | No | No | Yes (declarative UI in XML) |
| **Scene Builder** | No | No | Yes (visual drag-and-drop designer) |
| **Media/3D** | No | No | Yes (MediaPlayer, MediaView, 3D shapes) |

---

## 13.2 AWT (Abstract Window Toolkit)

### AWT Hierarchy
```
java.lang.Object
  │
  └─ java.awt.Component (abstract)
       │
       ├─ Button
       ├─ Label
       ├─ TextField
       ├─ TextArea
       ├─ Checkbox
       ├─ Choice
       ├─ List
       ├─ Scrollbar
       ├─ Canvas
       └─ Container
            │
            ├─ Panel
            ├─ Window
            │    │
            │    ├─ Frame
            │    └─ Dialog
            ├─ Applet (deprecated)
            └─ ScrollPane
```

### Key Classes with Packages

| Class | Package | Description |
|-------|---------|-------------|
| **Component** | `java.awt` | Abstract base class; all GUI elements extend this |
| **Container** | `java.awt` | Extends Component; holds other components, manages layout |
| **Panel** | `java.awt` | Concrete Container; no title bar/border; default FlowLayout |
| **Window** | `java.awt` | Top-level window; no title bar, cannot be minimized |
| **Frame** | `java.awt` | Top-level window with title bar, menu bar, resizable borders |
| **Button** | `java.awt` | Push button; generates `ActionEvent` |
| **Label** | `java.awt` | Non-editable text display; supports alignment |
| **TextField** | `java.awt` | Single-line text input; generates `ActionEvent` on Enter |
| **TextArea** | `java.awt` | Multi-line text input with scrollbar support |
| **Checkbox** | `java.awt` | On/off toggle; can be grouped via `CheckboxGroup` |
| **Choice** | `java.awt` | Dropdown list (single selection) |
| **List** | `java.awt` | Multiple item selection; single/multi mode |
| **Canvas** | `java.awt` | Blank area for custom drawing (`paint(Graphics g)`) |
| **Scrollbar** | `java.awt` | Scroll control (horizontal/vertical) |
| **Dialog** | `java.awt` | Modal/non-modal dialog; `FileDialog` extends it |

### AWT Event Handling (Delegation Model)
```java
import java.awt.*;
import java.awt.event.*;

public class AWTEventExample extends Frame implements ActionListener, WindowListener {
    private TextField tf;
    private Label status;
    
    AWTEventExample() {
        setTitle("AWT Event Handling");
        setSize(400, 250);
        setLayout(new FlowLayout(15));
        
        Label lbl = new Label("Enter name:");
        tf = new TextField(20);
        Button btn = new Button("Click Me");
        status = new Label("Ready");
        
        // Register listeners
        tf.addActionListener(this);
        btn.addActionListener(this);
        addWindowListener(this);
        
        add(lbl);
        add(tf);
        add(btn);
        add(status);
        
        setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == tf) {
            status.setText("TextField: " + tf.getText());
        } else if (e.getSource() instanceof Button) {
            status.setText("Hello, " + tf.getText() + "!");
        }
    }
    
    @Override
    public void windowClosing(WindowEvent e) {
        dispose();
        System.exit(0);
    }
    
    // Other WindowListener methods (empty but required)
    @Override public void windowOpened(WindowEvent e) {}
    @Override public void windowClosed(WindowEvent e) {}
    @Override public void windowIconified(WindowEvent e) {}
    @Override public void windowDeiconified(WindowEvent e) {}
    @Override public void windowActivated(WindowEvent e) {}
    @Override public void windowDeactivated(WindowEvent e) {}
    
    public static void main(String[] args) {
        new AWTEventExample();
    }
}
```

### AWT Button with Runnable for Threading Example
```java
// AWT uses single-threaded model; UI updates block
Button btn = new Button("Long Task");
btn.addActionListener(e -> {
    // UI freezes during this operation
    try { Thread.sleep(3000); } catch (InterruptedException ex) {}
});
```

---

## 13.3 Swing

### Swing Hierarchy
```
java.lang.Object
  │
  └─ java.awt.Component
       │
       └─ java.awt.Container
            │
            └─ javax.swing.JComponent (Swing base - lightweight)
                 │
         ┌───────┼───────┬────────┬────────┐
         ▼       ▼       ▼        ▼        ▼
      JButton  JLabel  JTextField JTable   JPanel
      JList    JTree   JTabbedPane JComboBox JFrame
      JDialog  JApplet JScrollPane JProgressBar
```

### Swing Architecture & Key Concepts

- **Lightweight**: Written in pure Java - no native peers, truly platform-independent
- **Pluggable Look & Feel**: At runtime via `UIManager.setLookAndFeel()` - Metal (default), Nimbus, Windows, Windows Classic, GTK, Aqua (Mac)
- **MVC Architecture**: Most components use Model-View-Controller (e.g., `JTable` uses `TableModel`, `JList` uses `ListModel`)
- **Double Buffering**: Automatic double buffering for smooth rendering, reduces flicker
- **Action Architecture**: `Action` interface encapsulates behavior, text, icon, mnemonic
- **EDT (Event Dispatch Thread)**: All UI updates must happen on this single thread

### Common Components with Key Methods

| Component | Package | Description | Key Methods/Properties |
|-----------|---------|-------------|------------------------|
| `JFrame` | `javax.swing` | Main window; default close operation required | `setDefaultCloseOperation()`, `setLocationRelativeTo(null)` to center |
| `JPanel` | `javax.swing` | Container; lightweight; can set layout | `setLayout(new BorderLayout())` |
| `JButton` | `javax.swing` | Action button | `setIcon()`, `setMnemonic()`, `setAction()` |
| `JLabel` | `javax.swing` | Label; supports HTML (`<html>...`) | `setIcon()`, `setHorizontalAlignment()` |
| `JTextField` | `javax.swing` | Single-line input | `setEchoChar()` for password; `getPassword()` returns char[] |
| `JPasswordField` | `javax.swing` | Password input | `getPassword()` returns char[] (clear after use for security!) |
| `JTextArea` | `javax.swing` | Multi-line text area | `setLineWrap(true)`, `setWrapStyleWord(true)` |
| `JCheckBox` | `javax.swing` | Checkbox | `setSelected()`, `isSelected()` |
| `JRadioButton` | `javax.swing` | Radio button | Use `ButtonGroup` for mutual exclusion |
| `JComboBox<E>` | `javax.swing` | Dropdown selection | `addItem()`, `getSelectedItem()`, `setEditable(true)` |
| `JList<E>` | `javax.swing` | List widget | `setSelectionMode()`, cell renderer via `setCellRenderer()` |
| `JTable` | `javax.swing` | Tabular data | Column classes, `TableModel`, `setColumnSelectionAllowed()` |
| `JTree` | `javax.swing` | Hierarchical data | `setRootVisible()`, `setExpandedState()` |
| `JTabbedPane` | `javax.swing` | Tabs | `addTab()`, `setSelectedIndex()` |
| `JMenuBar`, `JMenu`, `JMenuItem` | `javax.swing` | Menus | `setMnemonic()`, `addSeparator()`, accelerator via `KeyStroke` |
| `JFileChooser` | `javax.swing` | File selection | `showOpenDialog()`, `showSaveDialog()` |
| `JOptionPane` | `javax.swing` | Dialog boxes | `showMessageDialog()`, `showInputDialog()`, static methods |
| `JScrollPane` | `javax.swing` | Scrollable viewport | `setViewportView()`, scrollbar policies (`HORIZONTAL_SCROLLBAR_AS_NEEDED`) |
| `JSlider` | `javax.swing` | Slider control | `setMin()`, `setMax()`, `setShowTickLabels()` |
| `JProgressBar` | `javax.swing` | Progress bar | Indeterminate: `setIndeterminate(true)` |

### Swing Event Handling

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SwingEventHandler extends JFrame {
    private JLabel status;
    private JTextField inputField;
    private JTextArea resultArea;
    
    SwingEventHandler() {
        setTitle("Swing Event Handling");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        
        // Top panel with input
        JPanel topPanel = new JPanel(new FlowLayout());
        topPanel.add(new JLabel("Enter text:"));
        inputField = new JTextField(20);
        JButton processBtn = new JButton("Process");
        status = new JLabel("Ready");
        
        topPanel.add(inputField);
        topPanel.add(processBtn);
        topPanel.add(status);
        add(topPanel, BorderLayout.NORTH);
        
        // Center with scrollable text area
        resultArea = new JTextArea(10, 30);
        resultArea.setLineWrap(true);
        resultArea.setWrapStyleWord(true);
        JScrollPane scroll = new JScrollPane(resultArea);
        scroll.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
        add(scroll, BorderLayout.CENTER);
        
        // Event Handlers using Lambda
        inputField.addActionListener(e -> processInput());  // Enter key
        processBtn.addActionListener(e -> processInput());
        
        // Mouse listener example
        resultArea.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                status.setText("MouseClicked at: " + e.getPoint());
            }
        });
        
        // Window listener
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                // Confirm before exit
                int result = JOptionPane.showConfirmDialog(
                    SwingEventHandler.this,
                    "Are you sure you want to exit?",
                    "Confirm Exit",
                    JOptionPane.YES_NO_OPTION
                );
                if (result == JOptionPane.YES_OPTION) {
                    dispose();
                    System.exit(0);
                }
            }
        });
        
        setLocationRelativeTo(null);
        setVisible(true);
    }
    
    private void processInput() {
        String text = inputField.getText();
        if (text.isEmpty()) {
            status.setText("Please enter some text");
            return;
        }
        String timestamp = java.time.LocalTime.now().toString();
        resultArea.append("[" + timestamp + "] " + text + "\n");
        inputField.setText("");
        inputField.requestFocus();
        status.setText("Processed: " + text);
    }
    
    public static void main(String[] args) {
        // Always use invokeLater for Swing to ensure EDT
        SwingUtilities.invokeLater(() -> new SwingEventHandler());
    }
}
```

### Swing vs AWT: Key Differences Table

| Aspect | AWT | Swing |
|--------|-----|-------|
| **Component Inheritance** | `Component` → `Button`, `Label`, `Frame` | `JComponent` → `JButton`, `JLabel`, `JFrame` |
| **Native Peers** | Each component has a native peer (OS-specific) | None - pure Java implementation |
| **Look & Feel** | Fixed, matches native OS | Pluggable, uniform across platforms |
| **Component Variety** | Basic components only | Rich components (tables, trees, combo boxes, etc.) |
| **Painting** | `paint(Graphics g)` method | `paintComponent(Graphics g)` with double buffering |
| **Threading** | Single-threaded (blocks on UI) | EDT (Event Dispatch Thread) - same single-threaded model |
| **Performance** | Slower due to native peer overhead | Faster (pure Java, optimized) |
| **Event Model** | Delegation (Action, Mouse, etc.) | Same + Action class for unified handling |

---

## 13.4 JavaFX

### Overview
- **Modern GUI platform** for rich client applications (desktop, mobile, embedded)
- **Scene Graph** architecture: tree of Nodes (`javafx.scene.Node`)
- **CSS Styling** with `-fx-` prefix for properties
- **FXML** for declarative UI definition (XML-based)
- **MVC Pattern**: Model (data) - View (FXML/CSS) - Controller (Java class)
- **Hardware Acceleration**: GPU-accelerated rendering via Prism pipeline
- **Module System** (JDK 9+): Separate modules (`javafx.graphics`, `javafx.controls`, `javafx.fxml`, `javafx.media`, `javafx.web`, `javafx.swing`)

### JavaFX Architecture

```
javafx.application.Application (abstract class)
    │
    ├─ Stage (top-level window; represents OS window)
    │    Properties: title, icon, resizable, fullScreen, opacity, scene
    │    Methods: show(), hide(), close(), setScene(), setMinWidth/Height()
    │    │
    │    └─ Scene (container for all content; single root node)
    │         Properties: width, height, fill, cursor, stylesheets
    │         Methods: getRoot(), setRoot(), getWindow()
    │         │
    │         └─ Root Node (Layout Pane or Group)
    │              │
    │              ├─ Controls (Button, Label, TextField, TableView, etc.)
    │              ├─ Shapes (Circle, Rectangle, Line, Path, etc.)
    │              ├─ Media (ImageView, MediaView)
    │              ├─ Charts (LineChart, BarChart, PieChart, etc.)
    │              ├─ 3D Nodes (Box, Sphere, Cylinder, MeshView)
    │              ├─ Effects (DropShadow, Glow, Reflection, etc.)
    │              └─ Transforms (Translate, Rotate, Scale, Shear)
    │
    └─ CSS Stylesheets (scene.getStylesheets().add("style.css"))
```

### Stage vs Scene (Exam Important)

| Aspect | Stage | Scene |
|--------|-------|-------|
| **Represents** | OS-level window (top-level container) | Content container (scene graph root) |
| **Purpose** | Top-level window with border, title bar | All visual elements in one "scene" |
| **Can have multiple?** | One primary stage; multiple secondary stages possible | Only one active scene per stage (can swap) |
| **Methods** | `show()`, `hide()`, `close()`, `setTitle()` | `getRoot()`, `setRoot()`, `getStylesheets()`, `getRoot()` |
| **Relationship** | `stage.setScene(scene)` | `scene.getWindow()` returns owning Stage |

### JavaFX Application Structure
```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.geometry.Pos;
import javafx.geometry.Insets;

public class JavaFXExample extends Application {
    @Override
    public void start(Stage primaryStage) {
        // 1. Create controls
        Label label = new Label("Welcome to JavaFX");
        Button btn = new Button("Click Me");
        
        // 2. Create layout (root node)
        VBox root = new VBox(10, label, btn);  // 10px spacing
        root.setAlignment(Pos.CENTER);
        root.setPadding(new Insets(20));
        root.setStyle("-fx-background-color: #f0f0f0; -fx-border-color: #ccc;");
        
        // 3. Create scene
        Scene scene = new Scene(root, 400, 300);
        // scene.getStylesheets().add(getClass().getResource("styles.css").toExternalForm());
        
        // 4. Configure stage
        primaryStage.setTitle("JavaFX Example");
        primaryStage.setScene(scene);
        primaryStage.setMinWidth(300);
        primaryStage.setMinHeight(200);
        primaryStage.setResizable(true);
        primaryStage.show();
    }
    
    @Override
    public void init() throws Exception {
        // Called before start(); good for loading data
        System.out.println("Initializing...");
    }
    
    @Override
    public void stop() throws Exception {
        // Called when app closes; cleanup resources
        System.out.println("Stopping...");
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

### JavaFX Thread Model
```java
// JavaFX Application Thread - ONLY for UI updates
// Run on FX thread automatically from launch()

// BAD: Updating UI from background thread
new Thread(() -> {
    label.setText("Updated"); // WRONG! Throws exception
}).start();

// GOOD: Use Platform.runLater()
new Thread(() -> {
    // Background work
    String result = heavyComputation();
    Platform.runLater(() -> label.setText(result)); // Correct
}).start();
```

---

## 13.5 JavaFX Features

### Key Features (JavaFX 8+)
1. **FXML** - XML-based UI markup; separates view from logic
2. **CSS Styling** - Web-style styling with `-fx-` prefix; pseudo-classes (`:hover`, `:pressed`)
3. **Scene Builder** - Visual drag-and-drop UI designer (GlScene Builder)
4. **Properties & Binding** - Observable properties (`StringProperty`, `IntegerProperty`); bidirectional binding
5. **Animations & Transitions** - `Timeline`, `KeyFrame`; Transitions: `TranslateTransition`, `RotateTransition`, `ScaleTransition`, `FadeTransition`, `FillTransition`, `PathTransition`, `ParallelTransition`, `SequentialTransition`
6. **3D Graphics** - `Box`, `Sphere`, `Cylinder`, `MeshView`, `Camera` (Perspective, Fixed), `Lighting`
7. **Media Support** - `MediaPlayer`, `MediaView` for audio/video; formats: MP3, MP4, WAV, etc.
8. **WebView** - Embedded WebKit browser; `WebEngine` for JavaScript interaction
9. **Printing API** - `javafx.print` package; `PrinterJob`, `PageLayout`
10. **Touch & Gestures** - Multi-touch support; `TouchEvent`, gesture events (rotate, scroll, zoom)
11. **Charts** - `LineChart`, `BarChart`, `PieChart`, `ScatterChart`, `AreaChart`, `BubbleChart`
12. **HTML Editor** - `HTMLEditor` for rich text editing
13. **Date/Time Pickers** - `DatePicker`, `TimePicker`, `DateTimePicker`
14. **Accessibility** - Screen reader support, keyboard navigation

---

## 13.6 JavaFX UI Components (Controls)

### Common Controls

| Control | Description | Key Methods/Properties |
|---------|-------------|------------------------|
| `Label` | Non-editable text; supports HTML (`<b>`, `<i>`) | `setText()`, `setGraphic()`, `setAlignment()` |
| `Button` | Action button | `setOnAction()`, `setCancelButton()`, `setDefaultButton()` |
| `TextField` | Single-line input | `setText()`, `getText()`, `setPromptText()`, `getPassword()` |
| `PasswordField` | Masked input; returns char[] from `getPassword()` | Security: clear the array after use! |
| `TextArea` | Multi-line text input | `appendText()`, `insertText()`, `deleteTextRange()` |
| `CheckBox` | Boolean toggle | `setSelected()`, `isSelected()`, `setToggleGroup()` |
| `RadioButton` | Exclusive selection | Add to `ToggleGroup` for mutual exclusion |
| `ToggleButton` | Button with on/off state | Part of a `ToggleGroup` can be multi-state |
| `ComboBox<T>` | Dropdown with editable option | `getSelectionModel().getSelectedItem()`, `setEditable(true)` |
| `ChoiceBox<T>` | Simple dropdown, non-editable | `getSelectionModel().getSelectedItem()` |
| `ListView<T>` | List widget with selection | `setOnMouseClicked()`, `getSelectionModel().getSelectedIndex()` |
| `TableView<T>` | Tabular data with sorting/filtering | `setItems()`, `getColumns()`, cell value factories |
| `TreeView<T>` | Hierarchical data (`TreeItem<T>`) | `setRoot()`, `getSelectionModel().getSelectedItem()` |
| `WebView` | Embedded WebKit browser | `getEngine().load(url)`, `executeScript(js)` |
| `ScrollPane` | Scrollable viewport | `setFitToWidth()`, `setFitToHeight()` |
| `MenuBar`/`Menu`/`MenuItem` | Menus with accelerators | `setOnAction()`, `setAccelerator(KeyCombination)` |
| `ToolBar` | Tool buttons container | Add buttons, labels, other controls |
| `TabPane` | Tabbed interface | `getTabs()`, `setSelectedTab()` |
| `SplitPane` | Resizable dividers | `getSplitAreas()`, `setDividerPosition()` |
| `Accordion` | Stack of `TitledPane` (only one expanded) | `getPanes()`, `setExpandedPane()` |
| `TitledPane` | Collapsible titled panel | `setText()`, `setContent()`, `setExpanded()` |
| `DatePicker` | Calendar date picker | `setValue(LocalDate)`, `getEditor()` |
| `ColorPicker` | Color selection dialog | `setValue(Color)` |
| `Slider` | Numeric range slider | `setValue()`, `setMin()`, `setMax()`, `setShowTickLabels()` |
| `ProgressBar` | Progress bar (0.0–1.0) | `setProgress()` or `setIndeterminate(true)` |
| `ProgressIndicator` | Circular progress spinner | `setProgress()`, indeterminate mode by default |
| `Chart` (LineChart, BarChart, PieChart, etc.) | Data visualization | `getData()`, series/items management |
| `HTMLEditor` | Rich text editor | `getHtmlPane()`, `setOnAction()` events |

---

## 13.7 JavaFX Layouts (Panes)

| Layout | Description | Key Properties/Methods |
|--------|-------------|------------------------|
| `VBox` | Vertical column container | `spacing`, `alignment`, `children` |
| `HBox` | Horizontal row container | `spacing`, `alignment`, `children` |
| `BorderPane` | Top, Left, Center, Right, Bottom regions | `setTop()`, `setCenter()`, `setLeft()`, `setRight()`, `setBottom()` |
| `GridPane` | Grid of rows/columns | `add(node, col, row)`, `setHgap()`, `setVgap()`, `getColumnSpan()`, `getRowSpan()` |
| `FlowPane` | Flowing wrap layout | `orientation`, `hgap`, `vgap`, `prefWrapLength` |
| `TilePane` | Uniform-sized tiles | `orientation`, `prefTileWidth`, `prefTileHeight`, `alignment` |
| `StackPane` | Stacked (z-order) layout; centering default | `setAlignment()` for repositioning |
| `AnchorPane` | Anchored to edges | `setLeftAnchor(node, value)`, `setRightAnchor(node, value)`, etc. |
| `Pane` | Base class; manual positioning | Use `setLayoutX()`, `setLayoutY()`, `setPrefWidth()`, `setPrefHeight()` |
| `Group` | No layout; positional only | Children layered in order added |

### Detailed Layout Examples

```java
// VBox - Vertical form
VBox vbox = new VBox(15);
vbox.setPadding(new Insets(20));
vbox.setAlignment(Pos.CENTER);
vbox.getChildren().addAll(
    new Label("User Registration"),
    new TextField(),
    new PasswordField(),
    new Button("Register")
);

// HBox - Toolbar with spacer
HBox toolbar = new HBox(10);
Button saveBtn = new Button("Save");
Button cancelBtn = new Button("Cancel");
Region spacer = new Region();
HBox.setHgrow(spacer, Priority.ALWAYS);
Button settingsBtn = new Button("Settings");
toolbar.getChildren().addAll(saveBtn, cancelBtn, spacer, settingsBtn);

// BorderPane - Main application window
BorderPane main = new BorderPane();
MenuBar menuBar = new MenuBar(new Menu("File", new MenuItem("Open"), new MenuItem("Save")));
TreeView<String> sidebar = new TreeView<>();
TabPane tabPane = new TabPane(new Tab("Home"), new Tab("Reports"));
Label statusBar = new Label("Ready");
statusBar.setStyle("-fx-background-color: #eee; -fx-padding: 5;");
main.setTop(menuBar);
main.setLeft(sidebar);
main.setCenter(tabPane);
main.setBottom(statusBar);

// GridPane - Login form with alignment
GridPane login = new GridPane();
login.setHgap(10); login.setVgap(10);
login.setPadding(new Insets(30));
TextField usernameField = new TextField();
usernameField.setPromptText("Username");
PasswordField passwordField = new PasswordField();
passwordField.setPromptText("Password");
Button loginBtn = new Button("Login");

login.addRow(0, new Label("Username:"), usernameField);
login.addRow(1, new Label("Password:"), passwordField);
login.add(loginBtn, 1, 2);
GridPane.setHalignment(loginBtn, HPos.RIGHT);

// Advanced: Conditional cell factory (TableRow styling)
table.setRowFactory(tv -> new TableRow<Person>() {
    {
        itemProperty().addListener((obs, old, item) -> {
            if (item != null && item.getAge() > 65) {
                setStyle("-fx-background-color: #ffeb3b;");
            } else {
                setStyle("");
            }
        });
    }
});
```

---

## 13.8 FXML (Declarative UI)

### What is FXML?
- **FXML** is an XML-based markup language for defining JavaFX UI structure
- **Purpose**: Separates UI definition (FXML) from application logic (Controller)
- **Benefits**: Cleaner code, easier collaboration (designers vs developers), CSS styling support
- **Loading**: Use `FXMLLoader` to load, parses FXML, injects `@FXML` fields, calls `initialize()`

### FXML Key Attributes

| Attribute | Value | Purpose | Example |
|-----------|-------|---------|---------|
| `fx:id` | String | Unique ID; injected into controller field | `<Button fx:id="saveBtn"/>` |
| `fx:controller` | Fully qualified class name | Links FXML to controller | `<VBox fx:controller="com.app.Controller"/>` |
| `fx:source` | File path | Include another FXML file | `<fx:include source="header.fxml"/>` |
| `fx:factory` | Method name | Factory method for creation | `<ListView fx:factory="createList"/>` |
| `fx:define` | (in templates) | Define reusable objects | `<fx:define><Color fx:id="myRed" fx:value="RED"/></fx:define>` |

### Event Handler Attributes in FXML

| Attribute | Format | Purpose |
|-----------|--------|---------|
| `onAction` | `#methodName` | Button/menu click |
| `onMouseClicked` | `#method` | Mouse click |
| `onKeyPressed` | `#method` | Key press |
| `onMouseEntered` | `#method` | Mouse enter |
| `onMouseExited` | `#method` | Mouse exit |

---

## 13.9 Event Handling in JavaFX

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

## 13.10 CSS Styling in JavaFX

### What is JavaFX CSS?
- JavaFX uses CSS (Cascading Style Sheets) for styling UI components
- Properties are prefixed with `-fx-` (e.g., `-fx-background-color`, `-fx-font-size`)
- Can be external (separate .css file) or inline (`node.setStyle()`)
- Supports CSS pseudo-classes: `:hover`, `:pressed`, `:focused`, `:disabled`

### CSS Syntax for JavaFX

```css
/* Global styles */
.root {
    -fx-background-color: linear-gradient(to bottom, #2c3e50, #3498db);
    -fx-font-family: "Segoe UI", Arial, sans-serif;
}

/* Control types */
.button {
    -fx-background-color: #3498db;
    -fx-text-fill: white;
    -fx-font-size: 14px;
    -fx-padding: 10 20;
    -fx-background-radius: 5;
    -fx-cursor: hand;
}

.button:hover {
    -fx-background-color: linear-gradient(to bottom, #2980b9, #1f618d);
    -fx-effect: dropshadow(gaussian, rgba(0,0,0,0.3), 5, 0, 0, 2);
}

.button:pressed {
    -fx-background-color: #1f618d;
    -fx-translate-y: 1;
}

.button:disabled {
    -fx-background-color: #bdc3c7;
    -fx-cursor: default;
}

.text-field {
    -fx-border-color: #bdc3c7;
    -fx-border-width: 1;
    -fx-background-color: white;
    -fx-padding: 5 10;
}

.text-field:focused {
    -fx-border-color: #3498db;
    -fx-border-width: 2;
}

.label-title {
    -fx-font-size: 24px;
    -fx-font-weight: bold;
    -fx-text-fill: #2c3e50;
}

/* Custom classes (use -style-class or setStyle in Java) */
.custom-panel {
    -fx-background-color: #ecf0f1;
    -fx-border-color: #bdc3c7;
    -fx-border-width: 1;
    -fx-padding: 15;
    -fx-margin: 10;
}
```

### Applying CSS

```java
// Method 1: Inline styling
button.setStyle("-fx-background-color: #ff5722; -fx-text-fill: white;");

// Method 2: External stylesheet (recommended)
scene.getStylesheets().add(getClass().getResource("styles.css")
                              .toExternalForm());

// Method 3: Add multiple stylesheets (later ones override earlier)
scene.getStylesheets().addAll(
    "file:/path/to/base.css",
    getClass().getResource("theme.css").toExternalForm()
);

// Method 4: Dynamically add
scene.getStylesheets().add("styles.css");
// For JAR resources, use getClass().getResource()
```

### Important CSS Properties

| Property | Description | Example |
|----------|-------------|---------|
| `-fx-background-color` | Background fill | `#ff0000`, `linear-gradient(...)` |
| `-fx-text-fill` | Text color | `white`, `rgba(255,255,255,0.8)` |
| `-fx-font-size` | Font size | `14px`, `1.2em`, `14pt` |
| `-fx-font-weight` | Font weight | `bold`, `normal`, `100-900` |
| `-fx-font-family` | Font name | `"Arial"`, `"Verdana"` |
| `-fx-padding` | Interior spacing | `10`, `10 20`, `10 20 10 20` |
| `-fx-margin` | Exterior spacing (containers) | `10` |
| `-fx-border-color` | Border color | `#ccc` |
| `-fx-border-width` | Border thickness | `1`, `2 1`, `2 1 2 1` |
| `-fx-border-radius` | Border rounded corners | `5`, `5 10` |
| `-fx-background-radius` | Background rounded corners | `5` |
| `-fx-spacing` | Gap between children | `10` (for VBox, HBox) |
| `-fx-effect` | Visual effects | `dropshadow(...)`, `glow(...)` |
| `-fx-opacity` | Transparency | `0.0` (transparent) to `1.0` (opaque) |
| `-fx-cursor` | Mouse cursor | `hand`, `crosshair`, `default`, `wait` |
| `-fx-alignment` | Content alignment | `center`, `top-left`, `CENTER` |

---

## 13.11 Properties and Binding (JavaFX Observable Pattern)

### Why Properties?
- JavaFX uses reactive programming; properties are observable
- Automatic UI updates when values change
- Built-in support for binding and validation

### Property Types
| Property Class | Wraps Type | Primary Use |
|----------------|------------|--------------|
| `StringProperty` | `String` | Text content, labels |
| `IntegerProperty` | `int` | Counters, indices |
| `BooleanProperty` | `boolean` | Visibility, toggle states |
| `DoubleProperty` | `double` | Sliders, positions |
| `FloatProperty` | `float` | Specialized float handling |
| `LongProperty` | `long` | Large integer values |
| `ObjectProperty<T>` | `T` | Custom objects |
| `ListProperty<T>` | `ObservableList<T>` | List-backed controls |
| `MapProperty<K,V>` | `ObservableMap<K,V>` | Map-backed controls |

### Creating and Using Properties
```java
import javafx.beans.property.*;

public class Person {
    private final StringProperty name = new SimpleStringProperty(this, "name", "");
    private final IntegerProperty age = new SimpleIntegerProperty(this, "age", 0);
    private final BooleanProperty adult = new SimpleBooleanProperty(this, "adult", false);
    
    // Name property
    public String getName() { return name.get(); }
    public void setName(String name) { this.name.set(name); }
    public StringProperty nameProperty() { return name; }
    
    // Age property (with validation)
    public int getAge() { return age.get(); }
    public void setAge(int age) { 
        this.age.set(age);
        this.adult.set(age >= 18);  // Auto-update dependent property
    }
    public IntegerProperty ageProperty() { return age; }
    
    // Adult property
    public boolean isAdult() { return adult.get(); }
    public BooleanProperty adultProperty() { return adult; }
}
```

### Binding Example
```java
// Unidirectional binding (source → target, target is read-only)
Label label = new Label();
TextField tf = new TextField();
Person person = new Person();

// Bind label text to property
label.textProperty().bind(person.nameProperty());

// Bind to another control's property
tf.textProperty().bindBidirectional(person.nameProperty());

// Computed binding (formula)
IntegerProperty a = new SimpleIntegerProperty(10);
IntegerProperty b = new SimpleIntegerProperty(20);
IntegerProperty sum = new SimpleIntegerProperty();

// sum = a + b (auto-updated when a or b changes)
sum.bind(a.add(b));
System.out.println(sum.get());  // 30
a.set(5);
System.out.println(sum.get());  // 25 (auto-updated)

// Complex binding with Bindings API
Label details = new Label();
details.textProperty().bind(
    Bindings.concat("Name: ", person.nameProperty(),
                   ", Age: ", person.ageProperty().asString(),
                   ", ", Bindings.when(person.adultProperty())
                             .then("Adult")
                             .otherwise("Minor"))
);

// Format number with precision
priceLabel.textProperty().bind(
    Bindings.format("Price: $%.2f", priceProperty)
);

// Bidirectional binding
TextField minSalary = new TextField();
TextField maxSalary = new TextField();
minSalary.textProperty().bindBidirectional(maxSalary.textProperty());
```

### Binding with Controls
```java
// Slider to Label binding
Slider slider = new Slider(0, 100, 50);
Label sliderLabel = new Label();
sliderLabel.textProperty().bind(slider.valueProperty().asString("%.0f"));

// ToggleGroup with RadioButton
RadioButton maleBtn = new RadioButton("Male");
RadioButton femaleBtn = new RadioButton("Female");
ToggleGroup group = new ToggleGroup();
maleBtn.setToggleGroup(group);
femaleBtn.setToggleGroup(group);

Label genderLabel = new Label("Gender: ");
genderLabel.textProperty().bind(
    Bindings.when(group.selectedItemProperty().isNull())
        .then("Not selected")
        .otherwise(Bindings.concat("Selected: ", 
            group.selectedItemProperty().getText()))
);

// Validation example
TextField emailField = new TextField();
Label validationLabel = new Label();
validationLabel.textProperty().bind(
    Bindings.when(PatternConverter.createStringBinding(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{8,}$",
        emailField.textProperty()).isValid())
    .then("Valid email")
    .otherwise("Invalid email format")
);
```

---

## 13.12 Adding HTML Content, Text and Text Effects

### WebView (HTML Content)
```java
import javafx.scene.web.WebView;
import javafx.scene.web.WebEngine;
import netscape.javascript.JSObject;

WebView webView = new WebView();
WebEngine engine = webView.getEngine();

// Load external URL
engine.load("https://www.example.com");

// Load HTML content string
engine.loadContent("<h1>Hello HTML</h1><p>Styled with JavaFX WebView</p>");

// Execute JavaScript from Java
engine.executeScript("document.setBackgroundColor('lightblue')");

// Java-to-JavaScript bridge
JSObject window = (JSObject) engine.executeScript("window");
window.setMember("javaApp", new JavaBridge());

// JavaScript-to-Java bridge
// In JavaScript: javaApp.handleMessage("Hello from JS!")

public class JavaBridge {
    public void handleMessage(String msg) {
        System.out.println("Received: " + msg);
    }
}
```

### Advanced Text and Effects

```java
import javafx.scene.text.*;
import javafx.scene.paint.*;
import javafx.scene.effect.*;

// Text with gradient fill
Text gradientText = new Text("Gradient Text");
LinearGradient gradient = new LinearGradient(0, 0, 1, 0, true, CycleMethod.NO_CYCLE,
    new Stop(0, Color.RED), new Stop(1, Color.YELLOW));
gradientText.setFill(gradient);

// Text with multiple effects
DropShadow ds = new DropShadow(5, Color.BLACK);
Glow glow = new Glow(0.5);
Blend blend = new Blend(BlendMode.MULTIPLY, ds, glow);
gradientText.setEffect(ds);

// 3D Texts
Rotate xRotate = new Rotate(30, Rotate.X_AXIS);
gradientText.getTransforms().add(xRotate);

// Image in JavaFX
ImageView imageView = new ImageView(new Image("file:photo.jpg"));
imageView.setFitWidth(300);
imageView.setPreserveRatio(true);
```

---

## 13.13 Animations & Media in JavaFX

### JavaFX Animations

```java
import javafx.animation.*;
import javafx.util.Duration;

// TranslateTransition - Move node
TranslateTransition translate = new TranslateTransition(Duration.seconds(2), node);
translate.setFromX(0); translate.setToX(200);
translate.play();

// FadeTransition - Opacity change
FadeTransition fade = new FadeTransition(Duration.seconds(1), node);
fade.setFromValue(1.0); fade.setToValue(0.0);

// ParallelTransition - Run multiple animations together
ParallelTransition parallel = new ParallelTransition(node, translate, fade);
parallel.play();

// SequentialTransition - Run animations one after another
SequentialTransition sequential = new SequentialTransition(node, fade, translate);
sequential.play();

// Timeline - Keyframe animation (most powerful)
Timeline timeline = new Timeline(
    new KeyFrame(Duration.ZERO, 
        new KeyValue(node.translateXProperty(), 0),
        new KeyValue(node.rotateProperty(), 0)),
    new KeyFrame(Duration.seconds(2), 
        new KeyValue(node.translateXProperty(), 300),
        new KeyValue(node.rotateProperty(), 360))
);
timeline.setCycleCount(Animation.INDEFINITE);
timeline.setAutoReverse(true);
timeline.play();

// Rotation Transition
RotateTransition rotate = new RotateTransition(Duration.seconds(1), node);
rotate.setByAngle(180);
rotate.setCycleCount(Animation.INDEFINITE);
rotate.play();

// Scale Transition
ScaleTransition scale = new ScaleTransition(Duration.millis(500), node);
scale.setByX(1.5); scale.setByY(1.5);
scale.setAutoReverse(true);
scale.play();
```

### Media Support (Audio/Video)

```java
import javafx.scene.media.*;
import javafx.util.Duration;

// MediaPlayer for audio/video
Media media = new Media(getClass().getResource("audio.mp3").toExternalForm());
MediaPlayer player = new MediaPlayer(media);

// Playback controls
player.play();
player.pause();
player.stop();
player.setVolume(0.5);
player.setMute(true);
player.setRate(1.5);  // 1.5x speed

// Seek to position
player.seek(Duration.seconds(30));

// MediaView for displaying video
MediaView mediaView = new MediaView(player);
mediaView.setFitWidth(640);
mediaView.setFitHeight(480);
mediaView.setPreserveRatio(true);
mediaView.setSmooth(true);
```

---

## 13.14 Important Exam Questions (PYQ Analysis)

### Critical Priority Topics (90%+ Probability - Must Master)

**2-Mark Questions:**
1. Difference between AWT and Swing (heavyweight vs lightweight, peers vs pure Java)
2. Difference between Swing and JavaFX (JFC vs Scene Graph, UIManager vs CSS)
3. What is JavaFX? Key features (Scene Graph, CSS, FXML, Animation, Media, 3D)
4. What is FXML? What is Scene Builder? (declarative UI, visual designer)
5. Difference between Stage and Scene (window vs content container)
6. What is Scene Graph? (tree structure of nodes, root → children)
7. List 5 JavaFX layout panes (VBox, HBox, BorderPane, GridPane, StackPane)
8. Difference between ChoiceBox and ComboBox (editable vs non-editable)
9. What is `-fx-` prefix in JavaFX CSS? (CSS property namespace)
10. Difference between `setOnAction()` and FXML `onAction` attribute

**5-Mark Questions:**
1. Explain AWT, Swing, JavaFX with detailed comparison table.
2. Explain JavaFX architecture (Stage, Scene, Scene Graph, Nodes).
3. Explain JavaFX layouts (VBox, HBox, BorderPane, GridPane) with code examples.
4. Explain event handling in JavaFX with lambda expressions.
5. Write a JavaFX program: Button click updates Label text.
6. Explain CSS styling in JavaFX with pseudo-classes (`:hover`, `:pressed`).
7. Explain FXML structure and `fx:id` attribute with example.
8. Explain Properties and Binding in JavaFX (StringProperty, bindBidirectional).
9. Differentiate between `ChoiceBox` and `ComboBox`.
10. Explain JavaFX Effects (DropShadow, Glow, Reflection) with code.

**10-Mark Questions (Must Prepare):**
1. **Explain AWT vs Swing vs JavaFX. Detail JavaFX features, components, layouts, event handling, CSS styling, and FXML.** (Appeared: 2021, 2022, 2023, 2024, 2025, 2026)
2. Write a complete JavaFX login form using GridPane layout with CSS styling.
3. Explain JavaFX Architecture in detail. Draw the Scene Graph hierarchy.
4. Create a JavaFX application demonstrating VBox, HBox, BorderPane layouts.
5. Write a JavaFX program using FXML with Controller class and event handling.
6. Explain JavaFX Animations (Timeline, TranslateTransition, FadeTransition) with example code.
7. Explain Properties and Binding in JavaFX with practical examples.
8. Design a JavaFX application with TableView, CheckBox, and RadioButton in a BorderPane layout.
9. Write a JavaFX program demonstrating CSS styling with pseudo-classes.
10. Explain the difference between StackPane and AnchorPane layouts.

### Programs to Practice (High Yield - Multiple Appearances)

1. ✅ **JavaFX Hello World** - Stage, Scene, Label, Button setup | 2021–2026
2. ✅ **Event Handling** - Button click → Label update using lambda | 2022–2026
3. ✅ **Layout - BorderPane** - MenuBar (top), TreeView (left), TabPane (center), Label (bottom) | 2024–2026
4. ✅ **Layout - GridPane Form** - Name, Email, Password fields with validation | 2022, 2025
5. ✅ **CSS Styling** - Button styling with `:hover` and `:pressed` states | 2024–2025
6. ✅ **FXML with Controller** - Login form with `@FXML` annotation | 2023–2025
7. ✅ **TableView** - Two-column table with observable data | 2024–2026
8. ✅ **Animations** - FadeTransition or TranslateTransition demonstration | 2025–2026
9. ✅ **Properties & Binding** - Slider value bound to Label | 2025, 2026
10. ✅ **Effects** - DropShadow on a Button or Label | 2024
11. ✅ **Menu and MenuItem** - File menu with accelerators (Ctrl+S) | 2025
12. ✅ **TabPane** - Multiple tabs with different content | 2025

---

## Summary of Unit 13

| Topic | Key Points |
|-------|------------|
| **AWT** | Heavyweight, native peers, platform-dependent, basic components (Button, Label, Frame, etc.), uses `java.awt` package |
| **Swing** | Lightweight, pure Java, pluggable L&F, MVC architecture, rich components, uses `javax.swing` package, runs on EDT |
| **JavaFX** | Modern, Scene Graph architecture, CSS styling (`-fx-` prefix), FXML support, hardware accelerated, uses `javafx.*` packages |
| **JavaFX Architecture** | Application → Stage (window) → Scene (content) → Root Node (Layout/Group) → Controls/Shapes/Media |
| **Stage** | Represents OS window; `show()`, `setTitle()`, `setScene()`; methods: `close()`, `minimize()`, `maximize()` |
| **Scene** | Contains all UI elements; `setRoot()`, `getStylesheets()`, `getRoot()`, `setFill()` |
| **Layouts** | VBox (vertical), HBox (horizontal), BorderPane (5 regions), GridPane (grid), StackPane (overlay), AnchorPane (anchored), FlowPane (flow), TilePane (uniform tiles) |
| **Controls** | Label, Button, TextField, PasswordField, TextArea, CheckBox, RadioButton, ComboBox, ChoiceBox, ListView, TableView, TreeView, DatePicker, ColorPicker, Slider, ProgressBar, MenuBar, TabPane, SplitPane |
| **Event Handling** | Lambda expressions (`setOnAction(e -> ...)`), EventHandler interface, FXML controllers (`@FXML`, `onAction="#method"`), event phases (capture, target, bubble) |
| **FXML** | XML-based UI definition; `fx:id`, `fx:controller`, `onAction`; loaded via `FXMLLoader` |
| **CSS** | `-fx-background-color`, `-fx-text-fill`, `-fx-font-size`, `-fx-padding`, `-fx-effect`; pseudo-classes `:hover`, `:pressed`, `:focused`, `:disabled` |
| **Effects** | DropShadow, Glow, Reflection, Blur, ColorAdjust, Blend, Lighting |
| **Animations** | Transitions: TranslateTransition, RotateTransition, ScaleTransition, FadeTransition; Timeline, KeyFrame |
| **Media** | MediaPlayer, MediaView; formats: MP3, MP4, WAV, etc. |
| **3D Graphics** | Box, Sphere, Cylinder, MeshView, Camera, Lighting |
| **Charts** | LineChart, BarChart, PieChart, ScatterChart, AreaChart, BubbleChart |
| **WebView** | Embedded WebKit engine; `load()`, `executeScript()`, Java-JS bridge |
| **Properties & Binding** | `StringProperty`, `IntegerProperty`, `BooleanProperty`; `bind()`, `bindBidirectional()`, `Bindings` API |

---

## Quick Reference: JavaFX Template

```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.geometry.*;
import javafx.fxml.FXMLLoader;

public class MyApp extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        // Option 1: Pure Java
        Button btn = new Button("Click");
        btn.setOnAction(e -> System.out.println("Clicked!"));
        
        VBox root = new VBox(10, new Label("Hello JavaFX"), btn);
        root.setAlignment(Pos.CENTER);
        root.setPadding(new Insets(20));
        
        Scene scene = new Scene(root, 400, 300);
        scene.getStylesheets().add(getClass().getResource("style.css").toExternalForm());
        stage.setScene(scene);
        
        // Option 2: With FXML
        // FXMLLoader loader = new FXMLLoader(getClass().getResource("view.fxml"));
        // Parent root = loader.load();
        // stage.setScene(new Scene(root));
        
        stage.setTitle("JavaFX App");
        stage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

## FXML + Controller + CSS Complete Example

```java
// LoginController.java
package com.example;

import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.event.ActionEvent;

public class LoginController {
    @FXML private TextField usernameField;
    @FXML private PasswordField passwordField;
    @FXML private Button loginBtn;
    @FXML private Label statusLabel;
    
    @FXML
    private void initialize() {
        statusLabel.setText("Enter credentials");
    }
    
    @FXML
    private void handleLogin(ActionEvent event) {
        String user = usernameField.getText().trim();
        String pass = new String(passwordField.getPassword());
        
        if (user.isEmpty() || pass.isEmpty()) {
            statusLabel.setText("Fill all fields!");
            statusLabel.setStyle("-fx-text-fill: red;");
            return;
        }
        
        if ("admin".equals(user) && "password".equals(pass)) {
            statusLabel.setText("Login successful!");
            statusLabel.setStyle("-fx-text-fill: green;");
        } else {
            statusLabel.setText("Invalid credentials");
            statusLabel.setStyle("-fx-text-fill: red;");
            passwordField.clear();
        }
    }
}
```

```xml
<!-- login.fxml -->
<?xml version="1.0" encoding="UTF-8"?>
<?import javafx.scene.layout.*?>
<?import javafx.scene.control.*?>
<?import javafx.geometry.*?>

<GridPane hgap="10" vgap="10" alignment="CENTER"
          xmlns:fx="http://javafx.com/fxml/1"
          fx:controller="com.example.LoginController">
    
    <Label text="Username:" GridPane.rowIndex="0" GridPane.columnIndex="0"/>
    <TextField fx:id="usernameField" prefWidth="200" GridPane.rowIndex="0" GridPane.columnIndex="1"/>
    
    <Label text="Password:" GridPane.rowIndex="1" GridPane.columnIndex="0"/>
    <PasswordField fx:id="passwordField" prefWidth="200" GridPane.rowIndex="1" GridPane.columnIndex="1"/>
    
    <Button fx:id="loginBtn" text="Login" onAction="#handleLogin"
            GridPane.rowIndex="2" GridPane.columnIndex="1"/>
    
    <Label fx:id="statusLabel" GridPane.rowIndex="3" GridPane.columnIndex="1"/>
</GridPane>
```

```css
/* style.css */
.root {
    -fx-background-color: linear-gradient(to bottom, #2c3e50, #3498db);
    -fx-font-family: "Segoe UI", Arial, sans-serif;
}

.button {
    -fx-background-color: #3498db;
    -fx-text-fill: white;
    -fx-font-weight: bold;
    -fx-padding: 10 20;
    -fx-background-radius: 5;
}

.button:hover {
    -fx-background-color: #2980b9;
}

.text-field {
    -fx-border-color: #bdc3c7;
    -fx-border-radius: 3;
}
```

---

## Common Mistakes to Avoid (Exam Critical)

1. **Not using `Platform.runLater()`** when updating UI from background thread in JavaFX
2. **Missing `setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)`** in Swing JFrame
3. **Forgetting `launch(args)` call** in JavaFX main method
4. **Using wrong CSS property prefix** - must use `-fx-` (not just `background-color`)
5. **Forgetting `fx:controller` in FXML** - controller methods won't be called
6. **Not marking controller fields with `@FXML`** - fields remain null
7. **Using `==` for String comparison** in event handling - use `.equals()`
8. **Wrong FXML attribute syntax** - should be `onAction="#methodName"` not `onAction="methodName"`
9. **Not calling `setVisible(true)` in Swing** or forgetting to show stage in JavaFX
10. **Missing padding/alignment** in layouts - UI looks cramped