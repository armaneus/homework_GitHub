import ROOT
h = ROOT.TH1F("h", "Homework Histogram", 1000, 0, 10)
for i in range(5000):
h.Fill(ROOT.gRandom.Gaus(5, 3))
print("Entries=", h.GetEntries())
EOF

