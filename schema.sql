-- Create beacon_messages table in Supabase
-- Run this in your Supabase SQL Editor

CREATE TABLE IF NOT EXISTS beacon_messages (
    id BIGSERIAL PRIMARY KEY,
    beacon_id TEXT,
    message_type TEXT,
    payload JSONB,
    temperature NUMERIC,
    humidity NUMERIC,
    battery_level NUMERIC,
    signal_strength INTEGER,
    received_at TIMESTAMPTZ NOT NULL,
    source_ip TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create index for faster queries
CREATE INDEX idx_beacon_messages_received_at ON beacon_messages(received_at DESC);
CREATE INDEX idx_beacon_messages_beacon_id ON beacon_messages(beacon_id);

-- Optional: Enable Row Level Security (RLS)
ALTER TABLE beacon_messages ENABLE ROW LEVEL SECURITY;

-- Optional: Create a policy to allow all operations (adjust based on your security needs)
CREATE POLICY "Enable all operations for authenticated users" ON beacon_messages
    FOR ALL
    USING (true)
    WITH CHECK (true);

-- Comment on table
COMMENT ON TABLE beacon_messages IS 'Stores messages received from WiFi/Bluetooth beacons';
