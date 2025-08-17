# Elevator Data Mapping Documentation

## Overview
This document defines the standardized data mapping process for converting proprietary elevator controller data formats into a unified schema for centralized monitoring and analysis.

## 1. Data Source Formats

### 1.1 Otis Elevator Controllers
```json
{
  "sourceFormat": "Otis Gen2",
  "nativeSchema": {
    "car_speed_mps": "float",
    "door_state": "enum[OPEN,CLOSED,OPENING,CLOSING]",
    "floor_position": "integer",
    "load_percentage": "float",
    "fault_codes": "array[string]",
    "temp_celsius": "float",
    "vibration_gal": "float",
    "last_service": "timestamp",
    "motor_current_a": "float"
  }
}
```

### 1.2 Schindler Controllers
```json
{
  "sourceFormat": "Schindler PORT",
  "nativeSchema": {
    "velocity": "float",
    "door_cycle_time": "float",
    "current_floor": "integer",
    "cabin_load_kg": "float",
    "error_list": "array[integer]",
    "ambient_temp": "float",
    "acceleration": "float",
    "maintenance_date": "date",
    "power_consumption": "float"
  }
}
```

### 1.3 ThyssenKrupp Controllers
```json
{
  "sourceFormat": "TKE MAX",
  "nativeSchema": {
    "speed_ms": "decimal",
    "door_status": "integer",
    "level": "integer",
    "weight_kg": "decimal",
    "alarm_codes": "string",
    "temperature": "decimal",
    "vibration_ms2": "decimal",
    "service_timestamp": "long",
    "energy_kwh": "decimal"
  }
}
```

## 2. Standardized Target Schema

### 2.1 Unified Data Model
```sql
-- Performance Metrics Table
CREATE TABLE performance_metrics (
    id UUID PRIMARY KEY,
    elevator_id UUID NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    
    -- Motion Data
    speed_mps DECIMAL(5,2) CHECK (speed_mps >= 0 AND speed_mps <= 10),
    acceleration_ms2 DECIMAL(6,3),
    vibration_ms2 DECIMAL(8,4),
    
    -- Door Operations
    door_state ENUM('open', 'closed', 'opening', 'closing'),
    door_cycle_time_sec DECIMAL(5,2) CHECK (door_cycle_time_sec > 0),
    
    -- Position & Load
    current_floor INTEGER CHECK (current_floor >= -10 AND current_floor <= 200),
    load_kg DECIMAL(8,2) CHECK (load_kg >= 0),
    load_percentage DECIMAL(5,2) CHECK (load_percentage >= 0 AND load_percentage <= 150),
    
    -- Environmental
    temperature_celsius DECIMAL(5,1) CHECK (temperature_celsius >= -20 AND temperature_celsius <= 60),
    
    -- Energy
    power_consumption_kw DECIMAL(8,3),
    energy_consumption_kwh DECIMAL(10,3),
    
    -- Status
    operational_status ENUM('normal', 'maintenance', 'fault', 'emergency'),
    
    CONSTRAINT valid_timestamp CHECK (timestamp <= NOW()),
    INDEX idx_elevator_timestamp (elevator_id, timestamp),
    INDEX idx_timestamp (timestamp)
);

-- Events Table
CREATE TABLE elevator_events (
    id UUID PRIMARY KEY,
    elevator_id UUID NOT NULL,
    event_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    
    -- Event Classification
    event_type ENUM('info', 'warning', 'error', 'critical', 'maintenance'),
    event_category ENUM('mechanical', 'electrical', 'software', 'safety', 'performance'),
    
    -- Error Information
    standardized_code VARCHAR(10) NOT NULL,
    original_code VARCHAR(50),
    manufacturer_specific_code VARCHAR(100),
    
    -- Description
    event_description TEXT NOT NULL,
    severity_level INTEGER CHECK (severity_level >= 1 AND severity_level <= 5),
    
    -- Resolution
    resolved_timestamp TIMESTAMP WITH TIME ZONE,
    resolution_notes TEXT,
    
    INDEX idx_elevator_events (elevator_id, event_timestamp),
    INDEX idx_event_type (event_type, severity_level)
);
```

## 3. Mapping Configurations

### 3.1 Otis to Standard Mapping
```yaml
otis_gen2_mapping:
  manufacturer: "Otis"
  controller_type: "Gen2"
  version: "1.0"
  
  field_mappings:
    # Speed conversion
    speed_mps:
      source_field: "car_speed_mps"
      data_type: "decimal"
      precision: 2
      validation:
        min: 0.0
        max: 10.0
      transformation: "direct_copy"
    
    # Door state mapping
    door_state:
      source_field: "door_state"
      data_type: "enum"
      mapping:
        "OPEN": "open"
        "CLOSED": "closed"
        "OPENING": "opening"
        "CLOSING": "closing"
    
    # Load conversion
    load_kg:
      source_field: "load_percentage"
      data_type: "decimal"
      precision: 2
      transformation: "percentage_to_weight"
      parameters:
        max_capacity_kg: 1000
        formula: "source_value * max_capacity_kg / 100"
    
    # Temperature (direct copy)
    temperature_celsius:
      source_field: "temp_celsius"
      data_type: "decimal"
      precision: 1
      validation:
        min: -20.0
        max: 60.0
    
    # Vibration unit conversion
    vibration_ms2:
      source_field: "vibration_gal"
      data_type: "decimal"
      precision: 4
      transformation: "gal_to_ms2"
      formula: "source_value / 100"  # 1 gal = 0.01 m/s²
    
    # Error code standardization
    standardized_code:
      source_field: "fault_codes"
      data_type: "varchar"
      transformation: "error_code_mapping"
      mapping_table: "otis_error_codes"
```

### 3.2 Schindler to Standard Mapping
```yaml
schindler_port_mapping:
  manufacturer: "Schindler"
  controller_type: "PORT"
  version: "1.0"
  
  field_mappings:
    speed_mps:
      source_field: "velocity"
      data_type: "decimal"
      precision: 2
      validation:
        min: 0.0
        max: 10.0
    
    door_cycle_time_sec:
      source_field: "door_cycle_time"
      data_type: "decimal"
      precision: 2
      validation:
        min: 3.0
        max: 30.0
    
    current_floor:
      source_field: "current_floor"
      data_type: "integer"
      validation:
        min: -10
        max: 200
    
    load_kg:
      source_field: "cabin_load_kg"
      data_type: "decimal"
      precision: 2
      validation:
        min: 0
        max: 5000
    
    temperature_celsius:
      source_field: "ambient_temp"
      data_type: "decimal"
      precision: 1
    
    vibration_ms2:
      source_field: "acceleration"
      data_type: "decimal"
      precision: 4
      transformation: "direct_copy"
    
    standardized_code:
      source_field: "error_list"
      data_type: "varchar"
      transformation: "schindler_error_mapping"
      mapping_table: "schindler_error_codes"
```

## 4. Data Transformation Rules

### 4.1 Unit Conversions
```python
class UnitConverter:
    @staticmethod
    def gal_to_ms2(gal_value):
        """Convert Gal (galileo) to m/s²"""
        return gal_value / 100.0
    
    @staticmethod
    def percentage_to_weight(percentage, max_capacity_kg):
        """Convert load percentage to weight in kg"""
        return (percentage * max_capacity_kg) / 100.0
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5.0 / 9.0
    
    @staticmethod
    def pounds_to_kg(pounds):
        """Convert pounds to kilograms"""
        return pounds * 0.453592
```

### 4.2 Error Code Standardization
```python
# Error code mapping tables
OTIS_ERROR_MAPPING = {
    "E001": "DOOR-001",  # Door sensor failure
    "E002": "MOTOR-001", # Motor overcurrent
    "E003": "BRAKE-001", # Brake engagement failure
    "W001": "DOOR-002",  # Door cycle time exceeded
    "W002": "LOAD-001",  # Overload condition
}

SCHINDLER_ERROR_MAPPING = {
    "1001": "DOOR-001",  # Door sensor failure
    "1002": "MOTOR-001", # Motor overcurrent
    "2001": "SAFETY-001", # Safety circuit open
    "3001": "COMM-001",  # Communication error
}

def standardize_error_code(manufacturer, original_code):
    """Convert manufacturer-specific error codes to standard format"""
    mapping_table = {
        "Otis": OTIS_ERROR_MAPPING,
        "Schindler": SCHINDLER_ERROR_MAPPING,
        "ThyssenKrupp": TKE_ERROR_MAPPING
    }
    
    return mapping_table.get(manufacturer, {}).get(original_code, "UNKNOWN-999")
```

## 5. Data Validation Rules

### 5.1 Business Rules
```python
class DataValidationRules:
    # Physical constraints
    MAX_ELEVATOR_SPEED = 10.0  # m/s
    MAX_ACCELERATION = 2.0     # m/s²
    MAX_TEMPERATURE = 60.0     # Celsius
    MIN_TEMPERATURE = -20.0    # Celsius
    MAX_LOAD = 5000.0         # kg
    
    # Operational constraints
    MIN_DOOR_CYCLE_TIME = 3.0  # seconds
    MAX_DOOR_CYCLE_TIME = 30.0 # seconds
    MAX_FLOORS = 200
    MIN_FLOORS = -10
    
    @classmethod
    def validate_performance_data(cls, data):
        errors = []
        
        # Speed validation
        if data.get('speed_mps', 0) > cls.MAX_ELEVATOR_SPEED:
            errors.append("Speed exceeds maximum limit")
        
        # Temperature validation
        temp = data.get('temperature_celsius')
        if temp and (temp < cls.MIN_TEMPERATURE or temp > cls.MAX_TEMPERATURE):
            errors.append("Temperature outside valid range")
        
        # Load validation
        load = data.get('load_kg', 0)
        if load > cls.MAX_LOAD:
            errors.append("Load exceeds maximum capacity")
        
        return errors
```

### 5.2 Data Quality Checks
```python
class DataQualityChecker:
    @staticmethod
    def check_data_completeness(record):
        """Check for required fields"""
        required_fields = ['elevator_id', 'timestamp', 'speed_mps']
        missing_fields = [field for field in required_fields if field not in record]
        return missing_fields
    
    @staticmethod
    def check_data_consistency(record):
        """Check for logical consistency"""
        issues = []
        
        # Door state vs speed consistency
        if record.get('door_state') in ['opening', 'closing'] and record.get('speed_mps', 0) > 0.1:
            issues.append("Elevator moving while doors operating")
        
        # Load vs floor position
        if record.get('current_floor') == 0 and record.get('load_kg', 0) == 0:
            # Potential issue if always no load at ground floor
            pass
        
        return issues
```

## 6. Implementation Process

### 6.1 Data Pipeline Flow
```
1. Data Ingestion
   ├── Receive raw data via XML/JSON
   ├── Parse manufacturer-specific format
   └── Validate basic structure

2. Schema Mapping
   ├── Identify source controller type
   ├── Load appropriate mapping configuration
   └── Apply field transformations

3. Data Validation
   ├── Type checking
   ├── Range validation
   ├── Business rule validation
   └── Data quality assessment

4. Standardization
   ├── Unit conversions
   ├── Error code mapping
   ├── Enum standardization
   └── Format normalization

5. Storage
   ├── Insert into standardized database
   ├── Update data quality metrics
   └── Trigger alerts if needed
```

### 6.2 Configuration Management
```yaml
# Mapping configuration versioning
mapping_configs:
  - manufacturer: "Otis"
    controller_type: "Gen2"
    version: "1.0"
    effective_date: "2024-01-01"
    config_file: "otis_gen2_v1.yaml"
  
  - manufacturer: "Schindler"
    controller_type: "PORT"
    version: "2.1"
    effective_date: "2024-06-01"
    config_file: "schindler_port_v2.1.yaml"
```

This mapping documentation ensures consistent data transformation across all elevator manufacturers while maintaining data integrity and enabling effective centralized monitoring and analysis.